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
    uploaded_at = models.DateTimeField(auto_now=True)
    add_location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(default="Enter comment here")

    def __str__(self):
        return f"{self.user}"