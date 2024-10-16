from app.bisnes_services.daos.brands_dao import BrandDao
from app.bisnes_services.shemas.brands_shemas import BrandsShemas


class BrandsService:
    async def set_brands_in_database(item: BrandsShemas) -> bool:
        if await BrandDao.add_item_in_database(name=item.name, country=item.country):
            return True
        return False
