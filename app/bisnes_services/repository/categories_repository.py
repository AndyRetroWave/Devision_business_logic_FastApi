from app.bisnes_services.daos.category_dao import CategoryDao
from app.bisnes_services.shemas.category_shemas import CategoriesShemas


class CategoriesService:
    async def set_categories_in_database(item: CategoriesShemas) -> bool:
        if await CategoryDao.add_item_in_database(name=item.name):
            return True
        return False
