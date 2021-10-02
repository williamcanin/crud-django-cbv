from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import SignUpView, ChangePasswordView


urlpatterns = [
    path(
        "sign-in/",
        LoginView.as_view(
            redirect_authenticated_user=True, template_name="authentication/login.html"
        ),
        name="sign-in",
    ),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password/change/",
        ChangePasswordView.as_view(),
        name="password_change",
    ),
]
