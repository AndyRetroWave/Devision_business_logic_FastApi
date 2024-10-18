from fastapi import HTTPException
from sqlalchemy import delete, select
from starlette.status import HTTP_401_UNAUTHORIZED

from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.brands import Brands
from app.database import async_session_maker


class BrandDao(BaseDao):
    model = Brands

    @classmethod
    async def delete_brand_item(cls, name):
        try:
            async with async_session_maker() as session:
                await session.execute(delete(cls.model).where(cls.model.name == name))
                await session.commit()
                return True
        except Exception:
            return None

    @classmethod
    async def get_item(cls, **kwargs):
        try:
            async with async_session_maker() as session:
                result = await session.execute(select(cls.model))
                return result.scalars().all()
        except Exception:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
