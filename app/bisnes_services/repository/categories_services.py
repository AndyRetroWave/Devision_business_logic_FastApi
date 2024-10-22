from app.bisnes_services.daos.category_dao import CategoryDao
from app.bisnes_services.shemas.category_shemas import CategoriesShemas


class CategoriesService:
    dao = CategoryDao()

    async def set_categories_in_database(self, item: CategoriesShemas) -> bool:
        if await self.dao.add_item(name=item.name):
            return True
        return False

    async def get_all_categories(self) -> bool:
        return await self.dao.get_item()
