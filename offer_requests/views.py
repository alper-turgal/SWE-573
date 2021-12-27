from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OfferRequests
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.models import Profile
from .forms import OfferRequestAnswerForm


# Create your views here.


@login_required
def list_my_offers_requests(request, id):
    requests_query = OfferRequests.objects.all().filter(related_offer_id=id, status=1)
    return render(request, "offer_requests/my_offers_requests_list.html",
                  {"requests": requests_query})


@login_required
def accept_my_offers_requests(request, id):
    request_obj = get_object_or_404(OfferRequests, id=id)
    status = 2
    user = get_object_or_404(User, id=request_obj.request_creator_id)
    profile = get_object_or_404(Profile, user_id=request_obj.request_creator_id)
    if request.method == "POST":
        form = OfferRequestAnswerForm(request.POST, instance=request_obj)
        if form.is_valid():
            response_form = form.save(commit=False)
            response_form.status = status
            response_form.save()
            return redirect("my_offers_list")
    else:
        form = OfferRequestAnswerForm()
    return render(request, "offer_requests/my_offers_requests_detail.html",
                  {"user": user, "profile": profile, "form": form})
