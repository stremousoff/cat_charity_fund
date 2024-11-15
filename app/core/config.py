from typing import Optional

from pydantic import BaseSettings, EmailStr
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):
    app_title: str
    app_description: str
    app_version: str
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"  # FAILED
    # tests/test_db.py::test_check_db_url - KeyError: 'default'
    auth_backend_name: str = "jwt"
    secret: str
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()

engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
