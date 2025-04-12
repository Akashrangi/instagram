from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, Post, Likes, Comments, Employee, Department, EmployeeDepartment
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from  django.db.models import F

@login_required(login_url='login/')
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
    # For status
    following_users = User.objects.filter(followers__follower=request.user)
    status_user = UserProfile.objects.filter(user__in = following_users)
    status_user_list = list()
    for data in status_user:
        status_user_list.append({
            "username": data.user.username,
            "profile_photo": data.profile_photo.url
        })

    # For suggestions users
    followers_users = User.objects.filter(following__following=request.user)

    return render(request, "base.html", {"posts": posts_list, "status_user": status_user_list})

def signup_view(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        fullname = request.POST["fullname"]
        profile_image = request.FILES["profile_img"]

        if User.objects.filter(username = username).exists():
            messages.warning(request, 'Username alredy exists.')
            return

        if username and password:
            user = User.objects.create_user(username=username, password=password)

            user_profile = UserProfile(user = user, full_name = fullname, profile_photo = profile_image)
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

def demo(request):
    return render(request, 'demo.html')

def upload_post(request):
    location = request.POST["Location"]
    post_image = request.FILES.get("FileInput")

    user = User.objects.get(username = request.user)

    post = Post(posts = post_image, add_location = location)
    post.user = user
    post.save()
    return HttpResponse('Your post uploaded.')