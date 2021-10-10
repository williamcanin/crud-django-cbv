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
from django.contrib import messages

# def get_cep(instance, name: str, context: dict):
#     import requests
#
#     if instance.request.method == 'GET':
#         cep = instance.request.GET.get(name)
#         cep = re.sub("[^0-9]", "", cep)
#         data = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
#         address_data = data.json()
#         if 'erro' not in address_data:
#             context["city"] = address_data['localidade']
#             context["uf"] = address_data['uf']
#             return address_data
#     return "CEP não encontrado."


def is_validate(obj):
    """Função para verficar se o campo de pesquisa
    foi preenchido antes de mandar a busca"""

    if obj != "" and obj is not None:
        return obj.strip()


class ClientList(LoginRequiredMixin, ListView):
    template_name = "clients/listing.html"
    login_url = reverse_lazy("sign-in")
    model = ClientModel

    def get_queryset(self):
        records = self.model.objects.filter()
        q = self.request.GET.get("q")
        s_type = self.request.GET.get("s_type")
        data_number = self.request.GET.get("data_number")
        page = self.request.GET.get("page", 1)

        if data_number == "10":
            paginator = Paginator(records, 10)
        elif data_number == "25":
            paginator = Paginator(records, 25)
        elif data_number == "50":
            paginator = Paginator(records, 50)
        elif data_number == "100":
            paginator = Paginator(records, 100)
        else:
            paginator = Paginator(records, 10)

        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            records = paginator.page(1)
        except EmptyPage:
            records = paginator.page(paginator.num_pages)

        if is_validate(q):
            if s_type == "cpf" or s_type == "cnpj":
                q = re.sub("[^0-9]", "", q)
                records = self.model.objects.filter(cpf_cnpj=q)
            elif s_type == "id":
                records = self.model.objects.filter(id=q)
            elif s_type == "name":
                records = self.model.objects.filter(name__icontains=q)

        return records

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
    # Apenas use o fields se não for usar o form_class
    # fields = '__all__'
    success_url = reverse_lazy("client_read")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        context["PHOTO_ENABLE"] = settings.PHOTO_ENABLE
        return context

    def form_valid(self, form):
        # Ao criar, faz referencia ao usuário logado.
        form.instance.created_by_user = self.request.user.username
        form.instance.update_by = self.request.user.username
        # Resgata mensagem de sucesso caso seja criado.
        messages.success(self.request, "Salvo com sucesso.")
        return super().form_valid(form)


class ClientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "clients/form.html"
    login_url = reverse_lazy("sign-in")
    permission_required = "clients.change_clientmodel"
    model = ClientModel
    form_class = ClientForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("client_details", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_url"] = settings.MEDIA_URL
        return context

    def form_valid(self, form):
        # Ao atualizar, faz referencia ao usuário logado.
        form.instance.update_by = self.request.user.username
        # Resgata mensagem de sucesso caso seja atualizado.
        messages.success(self.request, "Atualizado com sucesso.")
        return super().form_valid(form)


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
