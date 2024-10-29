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
    price_min: Decimal = None
    price_max: Decimal = None
    categories: str = None
    brand: str = None
    size: str = None
    color: str = None
