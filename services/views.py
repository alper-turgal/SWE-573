from django.shortcuts import render
from .models import ServiceCategory, ServiceSubcategory
from django.shortcuts import get_object_or_404


# Create your views here.
def list_service_categories(request):
    return render(request, "services/categories.html",
                  {"service_categories": ServiceCategory.objects.all()})


def detail_service_categories(request, id):
    #   service_subcategory_list = list(get_object_or_404(ServiceSubcategory, service_category_id=id))
    #   service_subcategory_list = get_object_or_404(ServiceSubcategory, service_category_id=id)
    service_subcategory_list = ServiceSubcategory.objects.filter(service_category_id=id)
    return render(request, "services/details.html",
                  {"service_subcategory_list": service_subcategory_list})