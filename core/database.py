from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings
from collections.abc import AsyncGenerator

engine = create_async_engine(settings.database_url, echo=settings.sql_logging)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# temp MONGO settings to be replaced in transaction card
client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.database_name]