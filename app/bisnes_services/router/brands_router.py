from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.bisnes_services.repository.brands_repository import BrandsService
from app.bisnes_services.shemas.brands_shemas import BrandsShemas

router_brands = APIRouter(prefix="/sneakers_brands", tags=["Бренд кросовок"])
repository_brand_servis = BrandsService()


@router_brands.post("/add_brands")
async def add_a_new_brands(item: BrandsShemas) -> dict:
    if await repository_brand_servis.set_brands_in_database(item):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


@router_brands.delete("/delete_brand")
async def delete_brands_name(name) -> dict:
    if await repository_brand_servis.delete_brands(name):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


@router_brands.get("/get_brands_all")
async def get_all_brands():
    try:
        return await repository_brand_servis.get_all_brands()
    except HTTPException:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
