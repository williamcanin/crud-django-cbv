from django import forms
from .models import ClientModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Column, Row, ButtonHolder


class ClientForm(forms.ModelForm):  # pragma: no coverage
    class Meta:
        model = ClientModel
        fields = (
            "client_type",
            "name_corporate",
            "email",
            "birth_date",
            "district",
            "state",
            "cpf_cnpj",
            "address",
            "photo",
            "sex",
            "rg",
            "cep",
            "complement_address",
            "number_address",
            "cell_phone",
            "phone",
            "city",
            "obs",
        )

        widgets = {
            "state": forms.Select(attrs={"class": "form-select clients-form__states"}),
            "sex": forms.Select(attrs={"class": "form-select clients-form__sex"}),
            "client_type": forms.Select(
                attrs={"class": "form-select clients-form__client_type"}
            ),
        }

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

