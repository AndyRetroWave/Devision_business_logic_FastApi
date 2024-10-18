from app.bisnes_services.daos.brands_dao import BrandDao
from app.bisnes_services.shemas.brands_shemas import BrandsShemas


class BrandsService:
    dao = BrandDao

    async def set_brands_in_database(self, item: BrandsShemas) -> bool:
        if await self.dao.add_item_in_database(name=item.name, country=item.country):
            return True
        return False

    async def delete_brands(self, name) -> bool:
        if await self.dao.delete_brand_item(name):
            return True
        return False

    async def get_all_brands(self) -> BrandsShemas:
        return await self.dao.get_item()
