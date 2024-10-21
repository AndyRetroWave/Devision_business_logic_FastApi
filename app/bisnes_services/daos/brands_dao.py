from asyncio.log import logger

from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.exc import SQLAlchemyError
from starlette.status import HTTP_401_UNAUTHORIZED

from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.brands import Brands
from app.database import async_session_maker


class BrandDao(BaseDao):
    model = Brands

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

    async def delete_brand_item(self, name):
        async def delete_operation(session, name):
            await session.execute(delete(self.model).where(self.model.name == name))
            return True

        return await self._execute_with_session(delete_operation, name)

    async def get_item(self):
        async def select_operation(session):
            result = await session.execute(select(self.model))
            return result.scalars().all()

        return await self._execute_with_session(select_operation)
