from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float
    stock: int