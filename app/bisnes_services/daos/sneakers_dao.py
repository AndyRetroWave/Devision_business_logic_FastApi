from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.sneakers import Sneakers


class SneakerDao(BaseDao):
    model = Sneakers
