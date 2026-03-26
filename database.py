from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker,async_session,AsyncSession)
from typing import Any,AsyncGenerator
from sqlalchemy  import create_engine


DATABASE_URL="postgresql+asyncpg://postgres:Admin@localhost:5432/backendavia"
engine = create_async_engine(DATABASE_URL,echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session