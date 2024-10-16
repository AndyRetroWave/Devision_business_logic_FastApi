from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.brands import Brands


class BrandDao(BaseDao):
    model = Brands
