from decimal import Decimal

from pydantic import BaseModel


class SneakerShemas(BaseModel):
    name: str
    brand_id: int
    category: int
    price: Decimal
    size: str
    color: str
    description: str
    image_url: str
