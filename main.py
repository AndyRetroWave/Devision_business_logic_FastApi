import uvicorn
from fastapi import FastAPI
from app.bisnes_services.router.brands_router import router_brands
from app.bisnes_services.router.categories_router import router_categories
from app.bisnes_services.router.sneakers_router import router_sneaker


app = FastAPI()

app.include_router(router_sneaker)
app.include_router(router_brands)
app.include_router(router_categories)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
