from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import Base, SessionLocal, engine
from .security import create_access_token, get_current_admin, get_current_user, get_db, get_password_hash, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MRV Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_default_admin(db: Session):
    existing = crud.get_user_by_email(db, "admin@example.com")
    if existing is None:
        admin_user = models.User(
            email="admin@example.com",
            name="System Admin",
            hashed_password=get_password_hash("admin123"),
            is_admin=True,
        )
        db.add(admin_user)
        db.commit()


def seed_products(db: Session):
    if db.query(models.Product).count() == 0:
        sample_products = [
            {"name": "Laptop Pro 14", "category": "Electronics", "price": 1499.99, "stock": 12, "is_active": True},
            {"name": "Wireless Mouse", "category": "Accessories", "price": 39.99, "stock": 28, "is_active": True},
            {"name": "Mechanical Keyboard", "category": "Accessories", "price": 89.00, "stock": 8, "is_active": True},
            {"name": "4K Monitor", "category": "Electronics", "price": 699.00, "stock": 5, "is_active": True},
            {"name": "Office Chair", "category": "Furniture", "price": 249.00, "stock": 15, "is_active": True},
        ]
        for item in sample_products:
            db.add(models.Product(**item))
        db.commit()


@app.on_event("startup")
def startup():
    db = SessionLocal()
    try:
        create_default_admin(db)
        seed_products(db)
    finally:
        db.close()


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/auth/login", response_model=schemas.TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/auth/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
    return current_user


@app.get("/api/dashboard/stats", response_model=schemas.DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    stats = crud.get_dashboard_stats(db)
    return stats


@app.get("/api/admin/users", response_model=List[schemas.UserResponse])
def list_users(db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    return crud.get_users(db)


@app.post("/api/admin/users", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db, user, is_admin=False)


@app.put("/api/admin/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    updated = crud.update_user(db, user_id, user_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@app.delete("/api/admin/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    deleted = crud.delete_user(db, user_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


@app.get("/api/admin/products", response_model=List[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    return crud.get_products(db)


@app.post("/api/admin/products", response_model=schemas.ProductResponse, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    return crud.create_product(db, product)


@app.put("/api/admin/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    updated = crud.update_product(db, product_id, product_update)
    if updated is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@app.delete("/api/admin/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db), admin: models.User = Depends(get_current_admin)):
    deleted = crud.delete_product(db, product_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
