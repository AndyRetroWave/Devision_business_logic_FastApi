from sqlalchemy import select

from app.bisnes_services.daos.base_dao import BaseDao, session_handler
from app.bisnes_services.models.sneakers import Sneakers


class SneakerDao(BaseDao):
    model = Sneakers

    @session_handler
    async def get_item_by_id(self, session, id):
        smpt = await session.execute(
            select(self.model).where(self.model.sneaker_id == id)
        )
        return smpt.scalar()

    @session_handler
    async def get_item_by_filer(self, session, **item):
        smtp = await session.execute(select(self.model).where(**item))
        return smtp.scalars().all()
