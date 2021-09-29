import re
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DetailView,
    DeleteView,
)
from .models import ClientModel
from .forms import ClientForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class ClientList(LoginRequiredMixin, ListView):
    template_name = "clients/listing.html"
    login_url = reverse_lazy("sign-in")
    model = ClientModel

    def get_queryset(self):
        found = self.model.objects.filter()
        q = self.request.GET.get("q")
        s_type = self.request.GET.get("s_type")
        data_number = self.request.GET.get("data_number")
        page = self.request.GET.get("page", 1)

        if data_number == "10":
            paginator = Paginator(found, 10)
        elif data_number == "25":
            paginator = Paginator(found, 25)
        elif data_number == "50":
            paginator = Paginator(found, 50)
        elif data_number == "100":
            paginator = Paginator(found, 100)
        else:
            paginator = Paginator(found, 10)

        try:
            found = paginator.page(page)
        except PageNotAnInteger:
            found = paginator.page(1)
        except EmptyPage:
            found = paginator.page(paginator.num_pages)

        if s_type == "cpf" or s_type == "cnpj":
            q = re.sub("[^0-9]", "", q)
            found = self.model.objects.filter(cpf_cnpj=q)
        elif s_type == "id":
            found = self.model.objects.filter(id=q)
        elif s_type == "name":
            found = self.model.objects.filter(name__icontains=q)

        return found

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        context["data_number"] = self.request.GET.get("data_number")
        return context


class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "clients/form.html"
    login_url = reverse_lazy("sign-in")
    # Usando o {{ perms.auth }} mostra os valores para usar no "permission_required"
    permission_required = "clients.add_clientmodel"
    model = ClientModel
    form_class = ClientForm
    # fields = '__all__'
    success_url = reverse_lazy("client_read")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        return context


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "clients/form.html"
    login_url = reverse_lazy("sign-in")
    permission_required = "clients.change_clientmodel"
    model = ClientModel
    form_class = ClientForm
    # fields = '__all__'
    # success_url = reverse_lazy('client_details')

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("client_details", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        return context


class ClientDetails(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ClientModel
    login_url = reverse_lazy("sign-in")
    permission_required = "clients.view_clientmodel"
    template_name = "clients/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        context["is_details"] = True
        return context


class ClientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ClientModel
    login_url = reverse_lazy("sign-in")
    permission_required = "clients.delete_clientmodel"
    template_name = "clients/delete_confirm.html"
    success_url = reverse_lazy("client_read")
