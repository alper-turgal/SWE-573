from django.db import models
from django.contrib.auth.models import User
from offers.models import ServiceOffer


# Create your models here.
class OfferRequests(models.Model):
    request_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    related_offer = models.ForeignKey(ServiceOffer, on_delete=models.CASCADE)
    offer_creator_id = models.IntegerField()
    message = models.TextField(default="Teklifinizle ilgileniyorum, teşekkürler..")
    response_message = models.TextField(default="Kabul ettiğiniz için teşekkürler, görüşmek üzere..")
    status = models.IntegerField(default=2)
