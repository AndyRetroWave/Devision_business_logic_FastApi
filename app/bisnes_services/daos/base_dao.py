from abc import ABC, abstractmethod

from sqlalchemy import insert

from app.database import async_session_maker


class BaseDaoInterface(ABC):
    @abstractmethod
    async def add_item(self, **kwargs) -> bool:
        """Добавление информации в базу"""


class BaseDao(BaseDaoInterface):
    model = None

    @classmethod
    async def add_item_in_database(cls, **kwargs) -> bool:
        try:
            async with async_session_maker() as session:
                sneakers = insert(cls.model).values(**kwargs)
                await session.execute(sneakers)
                await session.commit()
                return True
        except Exception:
            return False
