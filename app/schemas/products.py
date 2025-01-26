from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Numeric

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category: str
    price: Numeric
    stock: int

    class Config:
        from_attributes = True
