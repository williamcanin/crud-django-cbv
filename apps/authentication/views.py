from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy


class SignInView(LoginView):
    redirect_authenticated_user = True


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('sign-in')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user

    #     get_user = User.objects.get(username='wcanin1')
    #     read_only = Group.objects.get(name='read_only')
    #     read_only.user_set.add(get_user)

    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     username_ = self.request.POST.get("username")
    #     get_user = User.objects.get(username=username_)
    #     read_only = Group.objects.get(name='read_only')
    #     print(username_, get_user, read_only)
    #     get_user.groups.add(name='read_only')
    #     # read_only.user_set.add(name=username_)

    #     # read_only = Group.objects.get(name='read_only')
    #     # read_only.user_set.add(username_)

    #     # self.object = None
    #     return super().post(request, *args, **kwargs)
