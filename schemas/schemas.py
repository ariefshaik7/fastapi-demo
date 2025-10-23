from pydantic import BaseModel, EmailStr
from datetime import datetime


class ProductBase(BaseModel):
    id: int
    name: str
    description : str
    # in_stock: bool = True

class ProductCreate(BaseModel):
    name: str
    description : str

class Product(ProductBase):
    pass
    