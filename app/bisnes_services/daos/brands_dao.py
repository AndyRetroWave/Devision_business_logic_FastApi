from sqlalchemy import delete, select

from app.bisnes_services.daos.base_dao import BaseDao, session_handler
from app.bisnes_services.models.brands import Brands


class BrandDao(BaseDao):
    model = Brands

    @session_handler
    async def delete_item(self, session, name):
        search_data = await session.execute(
            select(self.model).where(self.model.name == name)
        )
        if search_data.scalar() is None:
            return False
        await session.execute(delete(self.model).where(self.model.name == name))
        return True
