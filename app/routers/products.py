from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.core.database import get_db
from psycopg2.extras import RealDictCursor
from app.schemas.products import Product
from app.schemas.common import ListResponse

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", response_model=List[Product])
async def get_products(db=Depends(get_db)):
    """
    Get all products from database
    """
    try:
        db.execute("SELECT * FROM products")
        products = db.fetchall()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting products: {str(e)}")

@router.get("/{id}", response_model=Product)
async def get_product(id: int, db=Depends(get_db)):
    """
    Get a specific product by ID
    """
    try:
        db.execute("SELECT * FROM products WHERE id = %s", (id,))
        product = db.fetchone()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting product: {str(e)}")

@router.get("/search/{name}", response_model=List[dict])
async def search_products(name: str, db=Depends(get_db)):
    """
    Search products by name
    """
    try:
        db.execute("SELECT * FROM products WHERE name ILIKE %s", (f"%{name}%",))
        products = db.fetchall()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in search: {str(e)}")

@router.get("/category/{category}", response_model=List[dict])
async def get_products_by_category(category: str, db=Depends(get_db)):
    """
    Get products by category
    """
    try:
        db.execute("SELECT * FROM products WHERE category = %s", (category,))
        products = db.fetchall()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting products by category: {str(e)}")
