from app.bisnes_services.daos.sneakers_dao import SneakerDao
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)
from app.logger import logger


class SneakerService:
    dao = SneakerDao()

    def _except_logger(func):
        async def wrapper(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)
            except Exception as e:
                logger.error(
                    "Произошла ошибка в SneakerService.{}".format(func.__name__)
                    + f"\n{str(e.__doc__)}"
                )
                raise Exception()

        return wrapper

    @_except_logger
    async def set_sneakers_in_database(self, item: SneakerShemas):
        if await self.dao.add_item(
            name=item.name,
            brand_id=item.brand_id,
            category=item.category,
            price=item.price,
            size=item.size,
            color=item.color,
            description=item.description,
            image_url=item.image_url,
        ):
            return True
        return False

    @_except_logger
    async def get_sneakers_by_id(self, id: int):
        result = await self.dao.get_item_by_id(id)
        if result:
            return result
        return False

    @_except_logger
    async def get_by_filter(self, item: SneakerFilterShemas):
        result = await self.dao.get_item_by_filter_all(item)
        if result:
            return result
        return False
