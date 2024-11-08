from decimal import Decimal

import strawberry


@strawberry.type
class SneakerType:
    name: str
    brand_id: int
    category: int
    price: Decimal
    size: str
    color: str
    description: str
    image_url: str
