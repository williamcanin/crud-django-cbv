# from django.shortcuts import render
import re
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import PersonModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# def is_validate(obj):
#     if obj != "" and obj is not None:
#         return obj.strip()


class PersonList(ListView):
    template_name = 'person/listing.html'
    model = PersonModel

    def get_queryset(self):
        found = self.model.objects.filter()
        q = self.request.GET.get('q')
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

        if s_type == "cpf":
            q = re.sub("[^0-9]", "", q)
            found = self.model.objects.filter(cpf=q)
        elif s_type == "id":
            found = self.model.objects.filter(id=q)
        elif s_type == "name":
            found = self.model.objects.filter(name__icontains=q)

        return found

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        context['data_number'] = self.request.GET.get("data_number")
        return context


class PersonCreate(CreateView):
    template_name = 'person/form.html'
    fields = '__all__'
    model = PersonModel
    success_url = reverse_lazy('person_read')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        return context


class PersonUpdate(UpdateView):
    template_name = 'person/form.html'
    fields = '__all__'
    model = PersonModel
    success_url = reverse_lazy('person_read')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        return context


class PersonDetails(DetailView):
    model = PersonModel
    template_name = 'person/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['media_url'] = settings.MEDIA_URL
        return context


class PersonDelete(DeleteView):
    model = PersonModel
    fields = '__all__'
    template_name = 'person/delete_confirm.html'
    success_url = reverse_lazy('person_read')
