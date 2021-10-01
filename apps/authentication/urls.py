from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import SignInView, SignUpView


urlpatterns = [
    path('sign-in/', SignInView.as_view(template_name='authentication/login.html'), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('password/', PasswordChangeView.as_view(template_name='authentication/password_change.html'), name='password_change'),
]
