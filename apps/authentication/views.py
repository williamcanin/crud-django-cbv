from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('sign-in')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
