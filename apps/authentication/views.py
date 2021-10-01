from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.urls import reverse_lazy


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('sign-in')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(*args, **kwargs)
