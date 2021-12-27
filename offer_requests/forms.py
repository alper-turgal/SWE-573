from django.forms import ModelForm
from django import forms
from .models import OfferRequests


class OfferRequestAnswerForm(ModelForm):
    class Meta:
        model = OfferRequests
        fields = ('response_message',)
        labels = {
            "response_message": "Mesaj"
        }
        widgets = {
            "response_message": forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, "placeholder": "mesajınızı yazın"})
        }
