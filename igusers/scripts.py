from igusers.models import *
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render
from django.core.files import File
import json

def scripts_view(request):
    return render(request, "scripts.html")

def import_user(request):
    for i in range(1, 11):
        username = "user" + str(i)
        # user = User.objects.create(username = username, password = "admin")

    image = open('/Users/akashrangi/Desktop/Projects/instagram/media/profile_photos/users.jpg', 'rb')
    print(f"==>> image: {File(image)}")
    return HttpResponse(json.dumps({"code": 1, "msg": "User imported sucessfully."}))