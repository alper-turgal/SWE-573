from django.db import models
from django.contrib.auth.models import User
from offers.models import ServiceOffer


# Create your models here.
class OfferRequests(models.Model):
    request_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    related_offer = models.ForeignKey(ServiceOffer, on_delete=models.CASCADE, related_name="requests")
    offer_creator_id = models.IntegerField()
    message = models.TextField(default="Teklifinizle ilgileniyorum, teşekkürler..")
    response_message = models.TextField(default="Kabul ettiğiniz için teşekkürler, görüşmek üzere..")
    is_cancelled = models.BooleanField(default=False)
    is_offer_cancelled = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
