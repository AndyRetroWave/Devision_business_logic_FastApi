from pydantic import BaseModel


class BrandsShemas(BaseModel):
    name: str
    country: str
