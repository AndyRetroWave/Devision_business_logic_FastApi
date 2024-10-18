from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy import insert, select

from app.database import async_session_maker


class BaseDaoInterface(ABC):
    @abstractmethod
    async def add_item(self) -> bool:
        """Добавление информации в базу"""

    @abstractmethod
    async def get_item(self) -> Any:
        """Получение инфы из базы данных"""


class BaseDao(BaseDaoInterface):
    model = None

    @classmethod
    async def add_item_in_database(cls, **kwargs) -> bool:
        try:
            async with async_session_maker() as session:
                smtp = insert(cls.model).values(**kwargs)
                await session.execute(smtp)
                await session.commit()
                return True
        except Exception:
            return False

    @classmethod
    async def get_item(cls, **kwargs) -> Any:
        try:
            async with async_session_maker() as session:
                smtp = select(cls.model).filter_by(**kwargs)
                await session.extcute(smtp)
                return await smtp.scalar()
        except Exception:
            return None
