from decimal import Decimal
from app.bisnes_services.daos.sneakers_dao import SneakerDao
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)


async def creation_dict_with_parameters_for_filter_sneakers(
    item: SneakerFilterShemas,
) -> dict:
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

    return filter_params


async def get_result_for_sneaker_with_filter_on_database(
    dao: SneakerDao,
    price_min: Decimal = None,
    price_max: Decimal = None,
    **filters_params: dict,
) -> SneakerShemas:
    # Если прописанны и мин и макс значения фильтра то выдаем результат
    if price_min is not None and price_max is not None:
        if price_min < price_max:
            result = await dao.get_item_by_filter_price_min_and_max(
                price_min, price_max, **filters_params
            )
        else:
            raise ValueError("price_min must be less than price_max")

    # Если прописан только мин значение фильтра то выдаем результат
    elif price_min is not None:
        result = await dao.get_item_by_filter_price_min(price_min, **filters_params)

    # Если прописан только макс занчение фильтра то выдаем результат
    elif price_max is not None:
        result = await dao.get_item_by_filter_price_max(price_max, **filters_params)

    # Если ничего не прописано то выдаем результат
    else:
        result = await dao.get_item_by_filter(**filters_params)
    return result if result is not None else None
