from django.db import models
from services.models import ServiceCategory, ServiceSubcategory, Service
from datetime import time
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class ServiceOffer(models.Model):
    offer_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    service_title = models.TextField(max_length=200, verbose_name="Title")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_subcategory = models.ForeignKey(ServiceSubcategory, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200, verbose_name="Service Name")
    service_description = models.TextField(max_length=200, verbose_name="Description")
    service_date = models.DateField(verbose_name="Date of Delivery")
    service_start_time = models.TimeField(default=time(9), verbose_name="Starting")
    service_duration = models.IntegerField(verbose_name="Duration (Hours)")
    service_new_duration = models.IntegerField(verbose_name="Duration (Hours)", default=0)
    service_spot = models.CharField(max_length=200, verbose_name="Lokasyon", default="Maçka Parkı")
    service_city = models.CharField(max_length=200, verbose_name="Your City")
    service_district = models.CharField(max_length=200, verbose_name="Your District")
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    is_requested = models.BooleanField(default=False)
    is_request_accepted = models.BooleanField(default=False)
    accepted_request_id = models.IntegerField(default=0)
    is_service_provider_finalized = models.BooleanField(default=False)
    is_service_taker_finalized = models.BooleanField(default=False)
    is_service_cancelled = models.BooleanField(default=False)
    request_count = models.IntegerField(default=0)
    service_rating = models.IntegerField(default=5)
    service_comment = models.CharField(default="Yorum yazabilirsiniz..", max_length=200, verbose_name="Yorumunuz")

    def __str__(self):
        return f"{self.service_name} on {self.service_date}"
