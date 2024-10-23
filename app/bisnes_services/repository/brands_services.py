from app.bisnes_services.daos.brands_dao import BrandDao
from app.bisnes_services.shemas.brands_shemas import BrandsShemas


class BrandsService:
    dao = BrandDao()

    async def set_item_brands(self, item: BrandsShemas) -> bool:
        if await self.dao.add_item(name=item.name, country=item.country):
            return True
        return False

    async def delete(self, name) -> bool:
        if await self.dao.delete_item(name):
            return True
        return False

    async def get_all(self) -> BrandsShemas:
        return await self.dao.get_item()
