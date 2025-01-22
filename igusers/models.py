from django.db import models
from django.contrib.auth.models import User
# Create your models here.0

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ImageField(upload_to="Posts")
    