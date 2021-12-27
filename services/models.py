from django.db import models


# Create your models here.
class ServiceCategory(models.Model):
    service_category = models.CharField('Service Category', max_length=200)

    def __str__(self):
        return self.service_category


class ServiceSubcategory(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_subcategory = models.CharField('Service Subcategory', max_length=200)

    def __str__(self):
        return self.service_subcategory


class Service(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_subcategory = models.ForeignKey(ServiceSubcategory, on_delete=models.CASCADE)
    service_name = models.CharField('Service Name', max_length=200)
