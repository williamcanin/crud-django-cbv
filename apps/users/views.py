from .forms import UserRegisterForm, UserCreationFormCustom
from django.views.generic.edit import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("sign-in")
    form_class = UserCreationFormCustom
    success_message = "Seu perfil foi criado com sucesso, basta fazer o login :)"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(*args, **kwargs)


class ChangePasswordView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("home_page")
    success_message = "Senha alterada com sucesso!"
