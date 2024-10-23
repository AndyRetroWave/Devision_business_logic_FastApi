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
        smtp = await session.execute(select(self.model).filter_by(**item))
        return smtp.scalars().all()

    @session_handler
    async def get_item_by_filter_price_min_and_max(
        self, session, price_min, price_max, **iter
    ):
        smtp = await session.execute(
            select(self.model)
            .where(
                self.model.price >= price_min,
                self.model.price <= price_max,
            )
            .filter_by(**iter)
        )
        return smtp.scalars().all()

    @session_handler
    async def get_item_by_filter_price_min(self, session, price_min, **iter):
        smtp = await session.execute(
            select(self.model).where(self.model.price >= price_min).filter_by(**iter)
        )
        return smtp.scalars().all()

    @session_handler
    async def get_item_by_filter_price_max(self, session, price_max, **iter):
        smtp = await session.execute(
            select(self.model).where(self.model.price <= price_max).filter_by(**iter)
        )
        return smtp.scalars().all()

    @session_handler
    async def get_item_by_filter(self, session, **iter):
        smtp = await session.execute(select(self.model).filter_by(**iter))
        return smtp.scalars().all()
