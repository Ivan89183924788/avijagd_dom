from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL="postgresql+asyncpg://postgres:Admin@localhost:5432/backendavia"
engine = create_async_engine(DATABASE_URL,echo=True)
sessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with sessionLocal() as session:
        yield session