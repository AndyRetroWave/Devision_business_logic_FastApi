from sqladmin import ModelView

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
