from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.brands import Brands


class CategoryDao(BaseDao):
    model = Brands
