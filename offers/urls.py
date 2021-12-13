from django.urls import path
from . import views

urlpatterns = [

    path("list/", views.list_all_offers, name="offers_list"),
    path("form/", views.give_services_offer_form, name="offer_form")

]
