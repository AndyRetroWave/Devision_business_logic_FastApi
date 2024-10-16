from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

DATABASE_PARAM: dict = {"poolclass": NullPool} if settings.MODE == "TEST" else {}
DATABASE_URL: str = (
    settings.db_connect if settings.MODE == "TEST" else settings.test_db_connect
)

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAM)
async_session_maker: sessionmaker = sessionmaker(  # type: ignore
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass
