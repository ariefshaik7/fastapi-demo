from pydantic import BaseModel, EmailStr
from datetime import datetime


class ProductBase(BaseModel):
    """
    Base schema for a Product.
    """
    name: str
    description: str
    # in_stock: bool = True


class ProductCreate(ProductBase):
    """
    Schema for creating a new product.
    """
    pass


class Product(ProductBase):
    """
    Schema for reading/returning a product.
    """
    id: int

    class Config:
        """
        Pydantic configuration.
        
        orm_mode = True tells Pydantic to read data even if it's an ORM model
        (e.g., a SQLAlchemy model) and not just a dict.
        """
        orm_mode = True


class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    """
    name: str
    email: EmailStr  
    password: str


class UserOut(BaseModel):
    """
    Schema for returning a user (public-facing).
    """
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """
        Pydantic configuration.
        
        orm_mode = True allows this model to be populated from a
        SQLAlchemy ORM object.
        """
        orm_mode = True


class Token(BaseModel):
    """
    Schema for the login response.
    
    This is what the user receives after a successful login,
    containing their authentication token.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Schema for the data embedded within a JWT.
    
    This defines the expected structure of the token's payload
    (e.g., the 'sub' field, which we use for the user's ID).
    """
    id: str | None = None