from pydantic import BaseModel
from typing import List, Generic, TypeVar

T = TypeVar('T')

class ErrorResponse(BaseModel):
    """Respuesta estándar de error"""
    detail: str

class ListResponse(BaseModel, Generic[T]):
    """Respuesta para listas de elementos"""
    items: List[T]
    total: int
