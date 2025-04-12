from django.urls import path
from . import views as allviews
from .scripts import *

urlpatterns = [
    path("", allviews.home, name="home"),
    path("sign-up/", allviews.signup_view, name="sign_up"),
    path("login/", allviews.login_view, name="login"),
    path("logout/", allviews.logout_view, name="logout"),
    path("upload_post/", allviews.upload_post, name="upload_post"),
    path("demo/", allviews.demo, name="demo"),
    path("import_user/", import_user, name="import_user"),
]