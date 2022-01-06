from django.urls import path
from . import views

urlpatterns = [

    path("categories/", views.list_service_categories, name="categories_list"),
    path("categories/<int:id>", views.detail_service_categories, name="category_detail"),
    path("search", views.search_for_service, name="service_search"),
    path("search/cat/<int:id>", views.list_according_to_service_category, name="service_search_cat"),
    path("search/cat/<str:city>", views.list_according_to_city_category, name="service_search_city"),

]
