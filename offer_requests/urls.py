from django.urls import path
from . import views

urlpatterns = [

    path("reqlist/<int:id>", views.list_my_offers_requests, name="request_list"),
    path("reqlistdet/<int:id>", views.accept_my_offers_requests, name="request_detail"),
]
