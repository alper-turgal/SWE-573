from django.shortcuts import render, redirect
from .models import ServiceOffer
from .forms import ServiceOfferForm, ServiceOfferEditForm, ServiceOfferFinalForm, OfferRequestForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile
from offer_requests.models import OfferRequests
from django.contrib import messages


@login_required
def list_all_offers(request):
    user = request.user
    offers = ServiceOffer.objects.all()
    return render(request, "offers/all_offers_list.html",
                  {"offers_list": offers, "in_user": user})


@login_required
def detail_all_offers(request, id):
    any_offer = get_object_or_404(ServiceOffer, id=id)
    my_recurring_requests = OfferRequests.objects.filter(request_creator=request.user, related_offer_id=id)

    return render(request, "offers/all_offers_detail.html", {"offer": any_offer, "check": my_recurring_requests})


# Cannot assign "6": "OfferRequests.request_creator" must be a "User" instance.
@login_required
def request_offer(request, id):
    req_offer = get_object_or_404(ServiceOffer, id=id)
    my_recurring_requests = OfferRequests.objects.filter(request_creator=request.user, related_offer_id=id)
    if my_recurring_requests.exists():
        messages.error(request, "Bu teklife daha önce talep göndermiştiniz!")
        return redirect("users-home")
    if request.method == "POST":
        requester = OfferRequests(request_creator=request.user, related_offer_id=id)
        form = OfferRequestForm(request.POST, instance=requester)
        profile = Profile.objects.get(user_id=request.user)
        offer_creator_id_in_req = req_offer.offer_creator_id
        credits_needed = req_offer.service_duration
        credits_existing = profile.credits
        if form.is_valid():
            if credits_existing >= credits_needed:
                profile.credits = profile.credits - credits_needed
                profile.save(update_fields=['credits'])
                req_offer.request_count += 1
                # req_offer.status = 2  # received demand
                req_offer.is_requested = True
                # req_offer.save(update_fields=['request_count', 'status', "is_requested"])
                req_offer.save(update_fields=['request_count', "is_requested"])
                post = form.save(commit=False)
                post.offer_creator_id = offer_creator_id_in_req
                post.save()
                return redirect("users-home")
            else:
                messages.error(request, "Bu servisi almak için yeterli krediniz yok!")
        else:
            form = ServiceOfferForm()
        return redirect("users-home")
    form = OfferRequestForm()
    creator_id = req_offer.offer_creator_id
    creator = User.objects.all().filter(id=creator_id)
    profile = Profile.objects.all().filter(user_id=creator_id)
    return render(request, "offers/offer_request.html",
                  {"creator": creator, "profile": profile, "form": form})


@login_required
def give_services_offer_form(request):
    if request.method == "POST":
        offer = ServiceOffer(offer_creator=request.user)
        form = ServiceOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect("users-home")
        else:
            form = ServiceOfferForm()
    form = ServiceOfferForm()
    return render(request, "offers/offer_create_form.html", {"form": form})


@login_required
def edit_services_offer_form(request, id):
    offer = get_object_or_404(ServiceOffer, id=id)
    if request.method == "POST":
        form = ServiceOfferEditForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect("users-home")
        else:
            form = ServiceOfferEditForm()
    form = ServiceOfferEditForm(instance=offer)
    return render(request, "offers/offer_edit_form.html", {"form": form})


@login_required
def delete_offer(request, id):
    offer = get_object_or_404(ServiceOffer, id=id)
    received_requests = OfferRequests.objects.filter(related_offer_id=id)
    credit_refund = offer.service_duration
    if request.method == "POST":
        offer.is_service_cancelled = True
        offer.save(update_fields=["is_service_cancelled"])
        for received_request in received_requests:
            received_request.is_offer_cancelled = True
            received_request.save(update_fields=["is_offer_cancelled"])
            if received_request.is_cancelled == False:
                if offer.is_request_accepted != True:
                    requester = get_object_or_404(Profile, user_id=received_request.request_creator_id)
                    requester.credits += credit_refund
                    requester.save(update_fields=["credits"])
                else:
                    accepted_request = get_object_or_404(OfferRequests, related_offer_id=offer.id)
                    requester = get_object_or_404(Profile, user_id=accepted_request.request_creator_id)
                    requester.credits += credit_refund
                    requester.save(update_fields=["credits"])
        # end of for loop
        return redirect("users-home")
    context = {"offer": offer}
    return render(request, "offers/offer_delete.html", context)


@login_required
def list_my_offers(request):
    my_offers = ServiceOffer.objects.all().filter(offer_creator_id=request.user.id)
    return render(request, "offers/my_offers_list.html",
                  {"my_offers_list": my_offers})


@login_required
def detail_my_offers(request, id):
    # my_offer = ServiceOffer.objects.all().filter(id=id)
    my_offer = get_object_or_404(ServiceOffer, id=id)
    return render(request, "offers/my_offers_detail.html", {"offer": my_offer})


@login_required
def finalize_service_as_provider(request, id):
    offer = get_object_or_404(ServiceOffer, id=id)
    # request_obj = get_object_or_404(OfferRequests, related_offer_id=id)
    if request.method == "POST":
        form = ServiceOfferFinalForm(request.POST, instance=offer)
        if form.is_valid():
            if offer.is_request_accepted == True:
                # offer_status = 4  # service provider confirmed
                # offer.is_service_provider_finalized = True
                final_form = form.save(commit=False)
                # final_form.status = offer_status
                final_form.is_service_provider_finalized = True
                final_form.save()
                # request_obj.status = offer_status
                # request_obj.save(update_fields=['status'])
                return redirect("users-home")
            else:
                messages.error(request, "Bu teklif için henüz onayladığınız bir talep yok!")
                return redirect("my_offers_list")
    form = ServiceOfferFinalForm()
    return render(request, "offers/offer_final_form.html", {"form": form})
