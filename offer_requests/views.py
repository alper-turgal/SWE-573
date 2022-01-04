from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OfferRequests
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.models import Profile
from .forms import OfferRequestAnswerForm, FinalizeServiceAsTakerForm
from django.contrib import messages
from offers.models import ServiceOffer


# Create your views here.


@login_required
def list_my_offers_requests(request, id):
    requests_query = OfferRequests.objects.all().filter(related_offer_id=id)

    return render(request, "offer_requests/my_offers_requests_list.html",
                  {"requests": requests_query})


@login_required
def accept_my_offers_requests(request, id):
    request_obj = get_object_or_404(OfferRequests, id=id)
    # offer_status = 3  # confirmed request
    # user = get_object_or_404(User, id=request_obj.request_creator_id)
    profile = get_object_or_404(Profile, user_id=request_obj.request_creator_id)
    offer = get_object_or_404(ServiceOffer, id=request_obj.related_offer_id)
    credit_refund = offer.service_duration
    # requests_received = OfferRequests.objects.all().filter(related_offer_id=offer.id)
    requests_received = offer.requests.all()
    if request.method == "POST":
        form = OfferRequestAnswerForm(request.POST, instance=request_obj)
        if form.is_valid():
            if offer.is_request_accepted != True:
                # offer.status = offer_status  # accepted demand
                offer.is_request_accepted = True
                offer.accepted_request_id = request_obj.id
                offer.save(update_fields=["is_request_accepted", "accepted_request_id"])
                # offer.save(update_fields=['status', "is_request_accepted"])
                # response_form = form.save(commit=False)
                # response_form.status = offer_status
                # response_form.save()
                for any_request in requests_received:
                    requesters_profile = get_object_or_404(Profile, user_id=any_request.request_creator_id)
                    if requesters_profile.user_id != request_obj.request_creator_id and any_request.is_cancelled == False:
                        requesters_profile.credits = requesters_profile.credits + credit_refund
                        requesters_profile.save(update_fields=["credits"])
                # profile.credits = profile.credits - credit_refund
                # profile.save(update_fields=["credits"])
                form.save()
                return redirect("my_offers_list")
            else:
                messages.error(request, "Bu teklif için kabul ettiğiniz bir talep var!")
                return redirect("my_offers_list")
    else:
        form = OfferRequestAnswerForm()
    return render(request, "offer_requests/my_offers_requests_detail.html",
                  {"offer": offer, "profile": profile, "form": form, "coming_request": request_obj})


def list_my_requests(request):
    my_requests = OfferRequests.objects.all().filter(request_creator=request.user)
    # request_status_wording = ["Boş", "Talep yok.", "Talebiniz bekliyor.", "Talebiniz kabul edildi.",
    # "Servis sunuldu, onayınız bekleniyor.","Tamamlandı"]
    # return render(request, "offer_requests/request_management.html",
    #              {"requests": my_requests, "my_status": request_status_wording})
    return render(request, "offer_requests/request_management.html",
                  {"requests": my_requests})


def detail_my_requests(request, id):
    offer_obj = get_object_or_404(ServiceOffer, id=id)
    my_request = get_object_or_404(OfferRequests, request_creator=request.user, related_offer_id=id)
    return render(request, "offer_requests/my_requests_detail.html",
                  {"offer": offer_obj, "my_request": my_request})


def finalize_service_as_taker(request, id):
    offer_obj = get_object_or_404(ServiceOffer, id=id)
    # request_obj = get_object_or_404(OfferRequests, related_offer_id=id)
    # offer_status = 5  # completed
    if request.method == "POST":
        form = FinalizeServiceAsTakerForm(request.POST, instance=offer_obj)
        if form.is_valid():
            response_form = form.save(commit=False)
            response_form.is_service_taker_finalized = True
            response_form.save()
            # response_form.status = offer_status
            new_offer_obj = get_object_or_404(ServiceOffer, id=id)
            credit_difference = offer_obj.service_new_duration - offer_obj.service_duration
            requester_profile = get_object_or_404(Profile, user=request.user)
            requester_profile.credits -= credit_difference
            requester_profile.save(update_fields=['credits'])
            provider_profile = get_object_or_404(Profile, user=offer_obj.offer_creator)
            provider_profile.credits += (credit_difference + offer_obj.service_duration)
            provider_profile.tot_hours_of_service += (credit_difference + offer_obj.service_duration)
            marginal_rating = new_offer_obj.service_rating * (
                    credit_difference + offer_obj.service_duration)
            existing_rating = provider_profile.average_rating * provider_profile.tot_hours_of_service
            provider_profile.average_rating = (marginal_rating + existing_rating) / (
                    provider_profile.tot_hours_of_service + (credit_difference + offer_obj.service_duration))
            provider_profile.save(update_fields=['credits', "tot_hours_of_service", "average_rating"])

            # request_obj.status = offer_status
            # request_obj.save(update_fields=['status'])
            return redirect("req_man")
    else:
        form = FinalizeServiceAsTakerForm()
    return render(request, "offer_requests/request_final_form.html",
                  {"form": form})


@login_required
def cancel_my_request(request, id):
    requested_offer = get_object_or_404(ServiceOffer, id=id)
    my_request = get_object_or_404(OfferRequests, request_creator=request.user, related_offer_id=id)
    my_profile = get_object_or_404(Profile, user_id=request.user.id)
    all_requests = OfferRequests.objects.all().filter(related_offer_id=id)
    if request.method == "POST":
        my_profile.credits += requested_offer.service_duration
        if requested_offer.request_count == 1:
            requested_offer.is_requested = False
        requested_offer.request_count -= 1
        if my_request.id == requested_offer.accepted_request_id:
            for other_request in all_requests:
                profile = get_object_or_404(Profile, user_id=other_request.request_creator_id)
                if profile.user_id != my_profile.user_id and other_request.is_cancelled == False:
                    if profile.credits >= requested_offer.service_duration:
                        profile.credits -= requested_offer.service_duration
                        profile.save(update_fields=["credits"])
                    else:
                        other_request.is_cancelled = True
                        other_request.save(update_fields=["is_cancelled"])
            requested_offer.accepted_request_id = 0
            requested_offer.is_request_accepted = False
        my_request.is_cancelled = True
        my_profile.save(update_fields=["credits"])
        requested_offer.save(
            update_fields=["request_count", "is_requested", "accepted_request_id", "is_request_accepted"])
        my_request.save(update_fields=["is_cancelled"])
        return redirect("req_man")
    return render(request, "offer_requests/cancel_request.html")
