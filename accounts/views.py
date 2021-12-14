from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register_page(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        messages.success(request, "Account was created for " + user)

        return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register_form.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("members")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/login_form.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")


# Create your views here.
from django.shortcuts import render


# Create your views here.
def welcome_members(request):
    return render(request, "accounts/memberpage.html")
