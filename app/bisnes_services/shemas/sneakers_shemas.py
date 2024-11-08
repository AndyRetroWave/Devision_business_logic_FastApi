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
    name: str | None = None
    price_min: Decimal | None = None
    price_max: Decimal | None = None
    categories: str | None = None
    brand: str | None = None
    size: str | None = None
    color: str | None = None
