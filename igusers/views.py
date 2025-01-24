from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, Post, Likes, Comments
from django.db.models import Count
# Create your views here.

def home(request):
    # all_posts = Post.objects.values(
    #     "user__username",
    #     "posts",
    #     "add_location",
    #     "uploaded_at"
    # )
    
    all_posts = Post.objects.prefetch_related('likes_set', 'comments_set').annotate(
        total_likes=Count('likes')  # Count the likes for each post
    )

    posts_list = list()
    for post in all_posts:
        posts_list.append({
            "user": post.user.username,
            "post_image": post.posts.url,
            "uploaded_at": post.uploaded_at,
            "location": post.add_location or "",
            "total_likes": post.total_likes,
            "comments": [
                {
                    "user": comment.user.username,
                    "comment": comment.comment,
                }
                for comment in post.comments_set.all().order_by("-id")[:1]
            ]
        })

    status_user = UserProfile.objects.all()
    status_user_list = list()
    for data in status_user:
        print(f"==>> data: {data}")
        status_user_list.append({
            "username": data.user.username,
            "profile_photo": data.profile_photo.url
        })

    return render(request, "base.html", {"posts": posts_list, "status_user": status_user_list})

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