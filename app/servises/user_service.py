from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import User
from sqlalchemy import select

class UserService(BaseModel):
    @staticmethod
    async def create_user(db:AsyncSession, email:str, password:str) -> User:
        user = User(email=email, password=password)
        db.add(user)
        await db.commit()

    @staticmethod
    async def login(db:AsyncSession, email:str,password:str) -> User:
        result=await db.execute(select(User).where(User.email==email))
        user=result.scalar_one_or_none()
        if not user or user.password!=password:
            return None
        return user