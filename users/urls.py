from django.urls import path
from .views import home, RegisterView, profile, show_profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('gen_profile/<int:id>', show_profile, name='gen_profile'),

]
