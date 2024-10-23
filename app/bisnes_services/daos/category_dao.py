from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.categories import Categories


class CategoryDao(BaseDao):
    model = Categories
