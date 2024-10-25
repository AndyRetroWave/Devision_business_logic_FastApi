from decimal import Decimal

from sqlalchemy import select

from app.bisnes_services.daos.base_dao import BaseDao, session_handler
from app.bisnes_services.models.sneakers import Sneakers
from app.bisnes_services.shemas.sneakers_shemas import SneakerShemas


class SneakerDao(BaseDao):
    model = Sneakers

    @session_handler
    async def get_item_by_id(self, session, id: int) -> SneakerShemas | None:
        smpt: SneakerShemas = await session.execute(
            select(self.model).where(self.model.sneaker_id == id)
        )
        return smpt.scalar() or None

    @session_handler
    async def get_item_by_filer(
        self, session, name: str, **item
    ) -> SneakerShemas | None:
        if name is not None:
            query = select(self.model).filter(self.model.name.like(f"%{name}%"))
        else:
            query = await session.execute(select(self.model).filter_by(**item))
        return query.scalars().all() or None

    @session_handler
    async def get_item_by_filter_price_min_and_max(
        self,
        session,
        price_min: Decimal,
        price_max: Decimal,
        name: str | None = None,
        **iter,
    ):
        query = select(self.model).where(
            self.model.price >= price_min,
            self.model.price <= price_max,
        )
        if name is not None:
            query = query.filter(self.model.name.like(f"%{name}%"))
        query = query.filter_by(**iter)
        query = await session.execute(query)
        return query.scalars().all() or None

    @session_handler
    async def get_item_by_filter_price_min(
        self, session, price_min: Decimal, name: str | None = None, **iter
    ) -> SneakerShemas | None:
        query = select(self.model).where(self.model.price >= price_min)
        if name is not None:
            query = query.filter(self.model.name.like(f"%{name}%"))
        query = query.filter_by(**iter)
        result = await session.execute(query)
        return result.scalars().all() or None

    @session_handler
    async def get_item_by_filter_price_max(
        self, session, price_max: Decimal, name: str | None = None, **iter
    ) -> SneakerShemas | None:
        query = select(self.model).where(self.model.price <= price_max)
        if name is not None:
            query = query.filter(self.model.name.like(f"%{name}%"))
        query = query.filter_by(**iter)
        result = await session.execute(query)
        return result.scalars().all() or None

    @session_handler
    async def get_item_by_filter(
        self, session, name: str | None = None, **iter
    ) -> SneakerShemas | None:
        query = select(self.model)
        if name is not None:
            query = query.filter(self.model.name.like(f"%{name}%"))
        query = query.filter_by(**iter)
        result = await session.execute(query)
        return result.scalars().all() or None
