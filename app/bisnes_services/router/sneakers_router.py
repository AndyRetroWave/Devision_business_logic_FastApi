from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.bisnes_services.repository.sneaker_repository import SneakerService
from app.bisnes_services.shemas.sneakers_shemas import SneakerShemas

router_sneaker = APIRouter(prefix="/sneakers", tags=["Кросовки"])


@router_sneaker.post("/add_sneaker")
async def add_a_new_model_of_sneakers(item: SneakerShemas) -> dict:
    if await SneakerService.set_sneakers_in_database(item):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
