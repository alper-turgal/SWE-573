from datetime import date
from django import forms
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError
from .models import ServiceOffer


class ServiceOfferForm(ModelForm):
    class Meta:
        model = ServiceOffer
        fields = "__all__"
        widgets = {
            "service_date": DateInput(attrs={"type": "date"}),
            "service_start_time": TimeInput(attrs={"type": "time"}),
            "service_duration": TextInput(attrs={"type": "number", "min": "1", "max": "3"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("service_date")
        if d < date.today():
            raise ValidationError("This is a past date.")
        return d
