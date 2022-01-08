from django.urls import path
from .views import home, RegisterView, profile, show_profile, show_my_profile, delete_my_profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('my_profile/', show_my_profile, name='my_profile'),
    path('deleteprofile/', delete_my_profile, name='delete_my_profile'),
    path('gen_profile/<int:id>', show_profile, name='gen_profile'),

]
