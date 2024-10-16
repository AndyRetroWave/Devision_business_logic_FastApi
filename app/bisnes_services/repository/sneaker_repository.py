from app.bisnes_services.daos.sneakers_dao import SneakerDao
from app.bisnes_services.shemas.sneakers_shemas import SneakerShemas


class SneakerService:
    async def setSneakerDaoin_database(item: SneakerShemas):
        if await SneakerDao.add_item_in_database(
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
