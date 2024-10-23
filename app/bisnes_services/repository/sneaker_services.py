from app.bisnes_services.daos.sneakers_dao import SneakerDao
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)


class SneakerService:
    dao = SneakerDao()

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

    async def get_sneakers_by_id(self, id: int):
        result = await self.dao.get_item_by_id(id)
        if result:
            return result
        return False

    async def get_by_filter(self, item: SneakerFilterShemas):
        filter_params = {}

        if item.name is not None:
            filter_params["name"] = item.name
        if item.brand_id is not None:
            filter_params["brand_id"] = item.brand_id
        if item.price_max is not None:
            filter_params["price_max"] = item.price_max
        if item.price_min is not None:
            filter_params["price_min"] = item.price_min
        if item.size is not None:
            filter_params["size"] = item.size
        if item.color is not None:
            filter_params["color"] = item.color

        price_min = filter_params.get("price_min")
        price_max = filter_params.get("price_max")

        filter_params.pop("price_min", None)
        filter_params.pop("price_max", None)

        if price_min is not None and price_max is not None:
            if price_min < price_max:
                result = await self.dao.get_item_by_filter_price_min_and_max(
                    price_min, price_max, **filter_params
                )
            else:
                raise ValueError("price_min must be less than price_max")
        elif price_min is not None:
            result = await self.dao.get_item_by_filter_price_min(
                price_min, **filter_params
            )
        elif price_max is not None:
            result = await self.dao.get_item_by_filter_price_max(
                price_max, **filter_params
            )
        else:
            result = await self.dao.get_item_by_filter(**filter_params)
        if result:
            return result
        return False
