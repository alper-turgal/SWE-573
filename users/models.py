from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #   avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    bio = models.TextField()
    credits = models.IntegerField(default=5)
    tot_hours_of_service = models.IntegerField(default=5)
    average_rating = models.IntegerField(default=5)

    def __str__(self):
        return self.user.username
