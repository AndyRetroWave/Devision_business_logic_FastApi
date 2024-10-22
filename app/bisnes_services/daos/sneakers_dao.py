from sqlalchemy import select
from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.sneakers import Sneakers
from app.database import async_session_maker


class SneakerDao(BaseDao):
    model = Sneakers

    async def get_item_by_id(self, id):
        async def get_operation(session, id):
            async with async_session_maker() as session:
                smpt = await session.execute(
                    select(self.model).where(self.model.sneaker_id == id)
                )
                return smpt.scalar()

        return await self._execute_with_session(get_operation, id)

    async def get_item_by_filer(self, **item):
        async def get_item_operatrion(session, **item):
            async with async_session_maker() as session:
                smtp = await session.execute(select(self.model).where(**item))
                return smtp.scalars().all()

        return await self._execute_with_session(get_item_operatrion, **item)
