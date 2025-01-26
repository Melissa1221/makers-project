from fastapi import HTTPException
from typing import List, Optional
from app.schemas.products import Product

class ProductService:
    def __init__(self, db):
        self.db = db

    def get_all_products(self) -> List[Product]:
        try:
            self.db.execute("""
                SELECT id, name, description, price, category, stock 
                FROM products
            """)
            return self.db.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        try:
            self.db.execute("""
                SELECT id, name, description, price, category, stock 
                FROM products 
                WHERE id = %s
            """, (product_id,))
            product = self.db.fetchone()
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")
            return product
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    def search_products_by_name(self, name: str) -> List[Product]:
        try:
            self.db.execute("""
                SELECT id, name, description, price, category, stock 
                FROM products 
                WHERE name ILIKE %s
            """, (f"%{name}%",))
            return self.db.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    def get_products_by_category(self, category: str) -> List[Product]:
        try:
            self.db.execute("""
                SELECT id, name, description, price, category, stock 
                FROM products 
                WHERE category = %s
            """, (category,))
            return self.db.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
