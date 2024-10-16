from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.bisnes_services.repository.categories_repository import CategoriesService
from app.bisnes_services.shemas.category_shemas import CategoriesShemas

router_categories = APIRouter(
    prefix="/sneakers_categories", tags=["Категории кросовок"]
)


@router_categories.post("/add_categories")
async def add_a_new_categories(item: CategoriesShemas) -> dict:
    if await CategoriesService.set_categories_in_database(item):
        return {"massege": HTTP_200_OK}
    raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
