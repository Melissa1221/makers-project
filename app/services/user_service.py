from fastapi import HTTPException
from typing import List, Optional
from app.schemas.users import User

class UserService:
    def __init__(self, db):
        self.db = db

    def get_all_users(self) -> List[User]:
        try:
            self.db.execute("SELECT id, name, email FROM users")
            return self.db.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            self.db.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
            user = self.db.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    def search_users_by_name(self, name: str) -> List[User]:
        try:
            self.db.execute("SELECT id, name, email FROM users WHERE name ILIKE %s", (f"%{name}%",))
            return self.db.fetchall()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
