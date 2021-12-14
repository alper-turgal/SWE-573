# Create your views here.
from django.shortcuts import render


# Create your views here.
def welcome_visitors(request):
    return render(request, "mysite/home.html")
