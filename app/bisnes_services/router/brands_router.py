from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.bisnes_services.repository.brands_repository import BrandsService
from app.bisnes_services.shemas.brands_shemas import BrandsShemas

router_brands = APIRouter(prefix="/sneakers_brands", tags=["Бренд кросовок"])


@router_brands.post("/add_brands")
async def add_a_new_brands(item: BrandsShemas) -> dict:
    if await BrandsService.set_brands_in_database(item):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
