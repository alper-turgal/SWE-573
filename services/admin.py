from django.contrib import admin
from .models import ServiceCategory, ServiceSubcategory, Service

# Register your models here.
admin.site.register(ServiceCategory)
admin.site.register(ServiceSubcategory)
admin.site.register(Service)
