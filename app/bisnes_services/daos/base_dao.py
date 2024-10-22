from asyncio.log import logger

from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from starlette.status import HTTP_401_UNAUTHORIZED

from app.database import async_session_maker


class BaseDao:
    model = None

    async def _execute_with_session(self, operation, *args, **kwargs):
        try:
            async with async_session_maker() as session:
                result = await operation(session, *args, **kwargs)
                await session.commit()
                return result
        except SQLAlchemyError as e:
            logger.error("Произошла ошибка базы", e)
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
        except Exception as e:
            logger.error("Произошла неизвестная ошибка в базе", e)
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    async def add_item(self, **kwargs) -> bool:
        async def insert_operation(session, **kwargs):
            smtp = insert(self.model).values(**kwargs)
            await session.execute(smtp)
            return True

        return await self._execute_with_session(insert_operation, **kwargs)

    async def get_item(self):
        async def select_operation(session):
            result = await session.execute(select(self.model))
            return result.scalars().all()

        return await self._execute_with_session(select_operation)
