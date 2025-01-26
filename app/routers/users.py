from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.core.database import get_db
from psycopg2.extras import RealDictCursor
from app.schemas.users import User
from app.schemas.common import ListResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=List[User])
async def get_users(db=Depends(get_db)):
    """
    Get all users from database
    """
    try:
        db.execute("SELECT * FROM users")
        users = db.fetchall()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting users: {str(e)}")

@router.get("/{id}", response_model=User)
async def get_user(id: int, db=Depends(get_db)):
    """
    Get a specific user by ID
    """
    try:
        db.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = db.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting user: {str(e)}")

@router.get("/search/{name}", response_model=List[dict])
async def search_users(name: str, db=Depends(get_db)):
    """
    Search users by name
    """
    try:
        db.execute("SELECT * FROM users WHERE name ILIKE %s", (f"%{name}%",))
        users = db.fetchall()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in search: {str(e)}")
