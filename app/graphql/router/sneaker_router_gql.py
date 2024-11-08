from decimal import Decimal

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.bisnes_services.repository.sneaker_services import SneakerService
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)
from app.graphql.models.models_gql import SneakerType


@strawberry.type
class SneakersGraphql:
    services = SneakerService()

    @strawberry.field
    @classmethod
    async def sneakers_get_item(
        cls,
        name: str = None,
        price_min: Decimal = None,
        price_max: Decimal = None,
        categories: str = None,
        brand: str = None,
        size: str = None,
        color: str = None,
    ) -> list[SneakerType]:
        item = SneakerFilterShemas(
            name=name,
            price_min=price_min,
            price_max=price_max,
            categories=categories,
            brand=brand,
            size=size,
            color=color,
        )

        result = await cls.services.get_by_filter(item)
        if result:
            return result
        return False

    @strawberry.mutation
    @classmethod
    async def add_sneaker(
        cls,
        name: str,
        brand_id: int,
        category: int,
        price: Decimal,
        size: str,
        color: str,
        description: str,
        image_url: str,
    ) -> SneakerType:
        item = SneakerShemas(
            name=name,
            brand_id=brand_id,
            category=category,
            price=price,
            size=size,
            color=color,
            description=description,
            image_url=image_url,
        )
        return await cls.services.set_sneakers_in_database(item=item)

    @strawberry.mutation
    @classmethod
    async def delete_sneakers(
        cls,
        id: int,
    ) -> str:
        if await cls.services.delete_sneakers_id_services(id):
            return "Кросовки успешно удалены!"
        return "Кроссовки не найдены."


schema = strawberry.Schema(SneakersGraphql)

graphql_app = GraphQLRouter(schema)
