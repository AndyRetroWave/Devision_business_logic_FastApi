from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.bisnes_services.repository.sneaker_services import SneakerService
from app.bisnes_services.shemas.sneakers_shemas import (
    SneakerFilterShemas,
    SneakerShemas,
)

router_sneaker = APIRouter(prefix="/sneakers", tags=["sneakers"])
sneaker_services = SneakerService()


@router_sneaker.post("/add_sneaker")
async def add_a_new_model_of_sneakers(item: SneakerShemas) -> dict:
    if await sneaker_services.set_sneakers_in_database(item):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


@router_sneaker.get("/get_sneakers/{id}")
async def get_sneaker_by_id(id: int):
    result = await sneaker_services.get_sneakers_by_id(id)
    if result:
        return result
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


@router_sneaker.get("/get_by_filter")
async def get_sneaker_by_filter(SneakerFilterShemas: SneakerFilterShemas):
    result = await sneaker_services.get_by_filter(SneakerFilterShemas)
    if result:
        return result
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
