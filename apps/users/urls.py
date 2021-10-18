from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, ChangePasswordView, SignInView


urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password/change/",
        ChangePasswordView.as_view(),
        name="password_change",
    ),
]
