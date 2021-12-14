from django.shortcuts import render, redirect
from .models import ServiceOffer
from .forms import ServiceOfferForm


# Create your views here.
def list_all_offers(request):
    return render(request, "offers/offers_list.html",
                  {"offers_list": ServiceOffer.objects.all()})


def give_services_offer_form(request):
    if request.method == "POST":
        form = ServiceOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("members")
        else:
            form = ServiceOfferForm()
    form = ServiceOfferForm()
    return render(request, "offers/offers_form.html", {"form": form})
