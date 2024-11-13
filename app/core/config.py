from pydantic import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    app_title: str
    app_description: str
    app_version: str
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
