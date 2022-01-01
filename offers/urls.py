from django.urls import path
from . import views

urlpatterns = [

    path("list/", views.list_all_offers, name="offers_list"),
    path("list/<int:id>", views.detail_all_offers, name="all_offers_detail"),
    path("myoffers/", views.list_my_offers, name="my_offers_list"),
    path("myoffers/<int:id>", views.detail_my_offers, name="my_offers_detail"),
    path("form/", views.give_services_offer_form, name="offers_form"),
    path("<int:id>/edit", views.edit_services_offer_form, name="offers_form_edit"),
    path("<int:id>/delete", views.delete_offer, name="offers_form_delete"),
    path("<int:id>/request", views.request_offer, name="offer_request"),
    path("<int:id>/finalize", views.finalize_service, name="offer_finalize"),

]
