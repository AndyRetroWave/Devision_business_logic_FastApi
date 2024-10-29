from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.bisnes_services.repository.brands_services import BrandsService
from app.bisnes_services.shemas.brands_shemas import BrandsShemas

router_brands = APIRouter(prefix="/sneakers_brands", tags=["Бренд кросовок"])
brand_servis = BrandsService()


@router_brands.post("/add_brands")
async def add_a_new_brands(item: BrandsShemas) -> dict:
    try:
        if await brand_servis.set_item_brands(item):
            return {"massege": HTTP_200_OK}
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)


@router_brands.delete("/delete_brand")
async def delete_brands_name(name) -> dict:
    try:
        if await brand_servis.delete(name):
            return {"massege": HTTP_200_OK}
        else:
            return {"massege": "Такого бренда нет в базе данных"}
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)


@router_brands.get("/get_brands_all")
async def get_all():
    try:
        return await brand_servis.get_all()
    except HTTPException:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)
