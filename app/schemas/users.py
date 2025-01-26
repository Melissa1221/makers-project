from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    is_admin: bool

    class Config:
        from_attributes = True
