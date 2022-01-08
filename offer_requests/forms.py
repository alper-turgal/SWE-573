from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField, Textarea
from django import forms
from .models import OfferRequests
from offers.models import ServiceOffer


class OfferRequestAnswerForm(ModelForm):
    class Meta:
        model = OfferRequests
        fields = ('response_message',)
        labels = {
            "response_message": "Your message:"
        }
        widgets = {
            "response_message": forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, "placeholder": "mesajınızı yazın"})
        }


class FinalizeServiceAsTakerForm(ModelForm):
    class Meta:
        model = ServiceOffer
        fields = ('service_rating', 'service_comment')
        labels = {
            "service_comment": "Your Comment"
        }

        widgets = {
            "service_rating": TextInput(attrs={"type": "number", "min": "1", "max": "5"}),
            'Yorum': Textarea(
                attrs={'class': 'form-control', 'rows': 3, "placeholder": "Yorumlarınızı yazabilirsiniz.."})
        }
