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


class SneakerFilterShemas(BaseModel):
    name: str = None
    brand_id: int = None
    price_min: Decimal = None
    price_max: Decimal = None
    size: str = None
    color: str = None
