from django.urls import path
from . import views

urlpatterns = [
    path("", views.goods_list, name='home'),
    path("new/", views.item_create, name="item-create"),
    path("edit/<int:pk>/", views.update_view, name="item-update"),

]