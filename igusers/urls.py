from django.urls import path
from . import views as allviews

urlpatterns = [
    path("", allviews.home, name="home"),
    path("sign-up/", allviews.signup_view, name="sign_up"),
    path("login/", allviews.login_view, name="login"),
    path("logout/", allviews.logout_view, name="logout"),
]