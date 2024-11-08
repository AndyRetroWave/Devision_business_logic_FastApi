# import sentry_sdk
# import uvicorn
# from fastapi import FastAPI
# from sqladmin import Admin

# from app.admin.Auth.admin_auth import AdminAuth
# from app.admin.model.model_admin import BrandAdmin, CategoriesAdmin, SneakerAdmin
# from app.bisnes_services.router.brands_router import router_brands
# from app.bisnes_services.router.categories_router import router_categories
# from app.bisnes_services.router.sneakers_router import router_sneaker
# from app.database import engine
# from app.graphql.router.sneaker_router_gql import graphql_app

# sentry_sdk.init(
#     dsn="https://03adb10cee695d57860c26149ea87e5e@o4506709859434496.ingest.us.sentry.io/4508221592829952",
#     traces_sample_rate=1.0,
#     _experiments={
#         "continuous_profiling_auto_start": True,
#     },
# )
# app = FastAPI()


# authentication_backend = AdminAuth(secret_key="...")
# admin = Admin(app, engine, authentication_backend=authentication_backend)
# admin.add_view(SneakerAdmin)
# admin.add_view(BrandAdmin)
# admin.add_view(CategoriesAdmin)

# app.include_router(router_sneaker)
# app.include_router(router_brands)
# app.include_router(router_categories)

# app.include_router(graphql_app, prefix="/graphql")

# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)


from contextlib import contextmanager


@contextmanager
def print_go_to_go():
    try:
        print("Привет")
        a = 1 / 0
        yield
    except Exception:
        msg = "Иди нахуй со своими приколами"
    finally:
        print("Пока")


with print_go_to_go() as go:
    print("друг")
