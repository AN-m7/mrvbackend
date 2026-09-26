from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=255)
    password: str = Field(..., min_length=6, max_length=255)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    is_admin: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    is_admin: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    category: str = Field(default="General", max_length=100)
    price: float = Field(..., ge=0)
    stock: int = Field(default=0, ge=0)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    is_active: Optional[bool] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DashboardStats(BaseModel):
    total_users: int
    total_products: int
    active_products: int
    low_stock_products: int
    total_revenue: float
    sales_trend: List[dict]
    category_breakdown: List[dict]
