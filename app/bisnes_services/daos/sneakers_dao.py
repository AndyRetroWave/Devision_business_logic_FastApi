from sqlalchemy import delete, select
from sqlalchemy.orm import sessionmaker

from app.bisnes_services.daos.base_dao import BaseDao, session_handler
from app.bisnes_services.models.brands import Brands
from app.bisnes_services.models.categories import Categories
from app.bisnes_services.models.sneakers import Sneakers
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)


class SneakerDao(BaseDao):
    model = Sneakers

    @session_handler
    async def get_item_by_id(
        self, session: sessionmaker, id: int
    ) -> SneakerShemas | None:
        smpt: SneakerShemas = await session.execute(
            select(self.model).where(self.model.sneaker_id == id)
        )
        return smpt.scalar() or None

    @session_handler
    async def get_item_by_filter_all(
        self, session: sessionmaker, item: SneakerFilterShemas
    ):
        query = select(self.model)
        filters = []
        if item.categories:
            filters.append(Categories.name == item.categories)
        if item.brand:
            filters.append(Brands.name == item.brand)
        if item.name:
            filters.append(self.model.name.like(f"%{item.name}%"))
        if item.price_min is not None:
            filters.append(self.model.price >= item.price_min)
        if item.price_max is not None:
            filters.append(self.model.price <= item.price_max)
        if item.color:
            filters.append(self.model.color == item.color)
        if item.size:
            filters.append(self.model.size == item.size)

        # Применяем фильтры к запросу
        if filters:
            query = query.where(*filters)

        result = await session.execute(query)
        return result.scalars().all() or None

    @session_handler
    async def delete_item_by_id(self, session: sessionmaker, id: int):
        search_data = await session.execute(
            select(self.model).where(self.model.sneaker_id == id)
        )
        if search_data.scalar() is None:
            return False
        await session.execute(delete(self.model).where(self.model.sneaker_id == id))
        return True
