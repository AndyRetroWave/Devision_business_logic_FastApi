from sqladmin import ModelView

from app.bisnes_services.models.brands import Brands
from app.bisnes_services.models.categories import Categories
from app.bisnes_services.models.sneakers import Sneakers


class SneakerAdmin(ModelView, model=Sneakers):
    column_list = "__all__"
    column_searchable_list = [
        Sneakers.sneaker_id,
        Sneakers.name,
        Sneakers.price,
        Sneakers.size,
        Sneakers.color,
    ]
    column_sortable_list = [
        Sneakers.sneaker_id,
        Sneakers.name,
        Sneakers.price,
        Sneakers.size,
        Sneakers.color,
    ]


class CategoriesAdmin(ModelView, model=Categories):
    colunm_list = "__all__"

    column_searchable_list = [
        Categories.categories_id,
        Categories.name,
    ]
    column_sortable_list = [
        Categories.categories_id,
        Categories.name,
    ]


class BrandAdmin(ModelView, model=Brands):
    column_list = "__all__"

    column_searchable_list = [
        Brands.brands_id,
        Brands.name,
    ]
    column_sortable_list = [
        Brands.brands_id,
        Brands.name,
    ]
