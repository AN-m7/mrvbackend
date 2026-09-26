from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from .security import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user_data: schemas.UserCreate, is_admin: bool = False):
    user = models.User(
        email=user_data.email,
        name=user_data.name,
        hashed_password=get_password_hash(user_data.password),
        is_admin=is_admin,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(models.User).order_by(models.User.created_at.desc()).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None

    if user_update.email is not None:
        db_user.email = user_update.email
    if user_update.name is not None:
        db_user.name = user_update.name
    if user_update.is_admin is not None:
        db_user.is_admin = user_update.is_admin

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user


def get_products(db: Session):
    return db.query(models.Product).order_by(models.Product.created_at.desc()).all()


def create_product(db: Session, product_data: schemas.ProductCreate):
    product = models.Product(
        name=product_data.name,
        category=product_data.category,
        price=product_data.price,
        stock=product_data.stock,
        is_active=product_data.is_active,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def update_product(db: Session, product_id: int, product_update: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None

    for field, value in product_update.model_dump(exclude_unset=True).items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return db_product


def get_dashboard_stats(db: Session):
    total_users = db.query(models.User).count()
    total_products = db.query(models.Product).count()
    active_products = db.query(models.Product).filter(models.Product.is_active == True).count()
    low_stock_products = db.query(models.Product).filter(models.Product.stock < 10).count()

    revenue_result = db.query(func.coalesce(func.sum(models.Product.price * models.Product.stock), 0)).scalar() or 0
    revenue_result = float(revenue_result)

    trend_result = db.query(
        models.Product.category.label("name"),
        func.sum(models.Product.stock).label("value")
    ).group_by(models.Product.category).all()

    sales_trend = [
        {"name": item.name or "General", "value": int(item.value)}
        for item in trend_result
    ]

    category_breakdown = [
        {"name": item.name or "General", "value": int(item.value)}
        for item in trend_result
    ]

    return {
        "total_users": total_users,
        "total_products": total_products,
        "active_products": active_products,
        "low_stock_products": low_stock_products,
        "total_revenue": revenue_result,
        "sales_trend": sales_trend,
        "category_breakdown": category_breakdown,
    }
