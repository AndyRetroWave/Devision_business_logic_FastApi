import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from app.admin.Auth.admin_auth import AdminAuth
from app.bisnes_services.router.brands_router import router_brands
from app.bisnes_services.router.categories_router import router_categories
from app.bisnes_services.router.sneakers_router import router_sneaker
from app.database import engine

from app.admin.model.model_admin import SneakerAdmin, BrandAdmin, CategoriesAdmin

app = FastAPI()

authentication_backend = AdminAuth(secret_key="...")
admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(SneakerAdmin)
admin.add_view(BrandAdmin)
admin.add_view(CategoriesAdmin)

app.include_router(router_sneaker)
app.include_router(router_brands)
app.include_router(router_categories)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
