from django.contrib import admin
from .models import UserProfile, Post, Likes, Comments
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comments)