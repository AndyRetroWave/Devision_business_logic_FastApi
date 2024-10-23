from app.bisnes_services.daos.sneakers_dao import SneakerDao
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)


class SneakerService:
    model = SneakerDao()

    async def set_sneakers_in_database(self, item: SneakerShemas):
        if await self.model.add_item(
            name=item.name,
            brand_id=item.brand_id,
            category=item.category,
            price=item.price,
            size=item.size,
            color=item.color,
            description=item.description,
            image_url=item.image_url,
        ):
            return True
        return False

    async def get_sneakers_by_id(self, id: int):
        result = await self.model.get_item_by_id(id)
        if result:
            return result
        return False

    async def get_by_filter(self, item: SneakerFilterShemas):
        name = item.name
        brand_id = item.brand_id
        price = item.price
        size = item.size
        color = item.color

        result = await self.model.get_item_by_filer(
            name=name,
            brand_id=brand_id,
            price=price,
            size=size,
            color=color,
        )
        if result:
            return result
        return False
