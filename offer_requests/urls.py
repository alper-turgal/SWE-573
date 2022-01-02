from django.urls import path
from . import views

urlpatterns = [

    path("reqlist/<int:id>", views.list_my_offers_requests, name="request_list"),
    path("reqlistdet/<int:id>", views.accept_my_offers_requests, name="request_detail"),
    path("reqman/", views.list_my_requests, name="req_man"),
    path("reqman/<int:id>", views.detail_my_requests, name="offer_detail"),
    path("<int:id>/reqfinalize", views.finalize_service_as_taker, name="request_finalize"),
]
