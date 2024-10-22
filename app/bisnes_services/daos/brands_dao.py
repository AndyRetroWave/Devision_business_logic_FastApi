from sqlalchemy import delete, select

from app.bisnes_services.daos.base_dao import BaseDao
from app.bisnes_services.models.brands import Brands


class BrandDao(BaseDao):
    model = Brands

    async def delete_brand_item(self, name):
        async def delete_operation(session, name):
            search_data = await session.execute(
                select(self.model).where(self.model.name == name)
            )
            if search_data.scalar() is None:
                return False
            await session.execute(delete(self.model).where(self.model.name == name))
            return True

        return await self._execute_with_session(delete_operation, name)
