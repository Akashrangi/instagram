from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile, Post, Likes, Comments, FollowUnfollow, Employee, Department, EmployeeDepartment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(FollowUnfollow)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(EmployeeDepartment)