from django.shortcuts import render
from .models import ServiceCategory, ServiceSubcategory
from offers.models import ServiceOffer
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


def search_for_service(request):
    categories = ServiceCategory.objects.all()
    cities = ServiceOffer.objects.values_list("service_city", flat=True).distinct()
    return render(request, "services/service_search.html",
                  {"categories": categories, "cities": cities})


def list_according_to_service_category(request, id):
    offers = ServiceOffer.objects.all().filter(service_category_id=id)
    service_category = get_object_or_404(ServiceCategory, id=id)
    user = request.user
    return render(request, "services/acc_to_category.html",
                  {"offers": offers, "category": service_category, "user": user})


def list_according_to_city_category(request, city):
    offers = ServiceOffer.objects.all().filter(service_city=city)
    city = city
    user = request.user
    return render(request, "services/acc_to_city.html",
                  {"offers": offers, "user": user, "city": city})
