from django.urls import path
from . import views

urlpatterns = [

    path("categories/", views.list_service_categories, name="categories_list"),
    path("categories/<int:id>", views.detail_service_categories, name="category_detail"),

]