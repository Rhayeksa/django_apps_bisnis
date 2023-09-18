from django.urls import path

from .views import add, detail, detele, edit, index

app_name = "kontak"

urlpatterns = [
    path(route="", view=index, name="index"),
    path(route="add/", view=add, name="add"),
    path(route="<int:id>/", view=detail, name="detail"),
    path(route="edit/<int:id>", view=edit, name="edit"),
    path(route="delete/<int:id>", view=detele, name="delete"),
]
