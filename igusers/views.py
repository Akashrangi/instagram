from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

def home(request):
    return render(request, "base.html")

def signup_view(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        fullname = request.POST["fullname"]
        biotext = request.POST["biotext"]
        profile_image = request.FILES["profile_img"]

        if username and password:
            user = User.objects.create_user(username=username, password=password)

            user_profile = UserProfile(user = user, full_name = fullname, bio = biotext, profile_photo = profile_image)
            user_profile.save()

            login(request, user)

            return redirect('home')
    return render(request, 'sign_up.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')