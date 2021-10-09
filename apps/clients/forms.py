from django import forms
from .models import ClientModel


class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = (
            "created_by_user",
            "name",
            "email",
            "birth_date",
            "district",
            "state",
            "cpf_or_cnpj",
            "cpf_cnpj",
            "address",
            "photo",
            "rg",
            "cep",
            "cell_phone",
            "phone",
            "city",
            "update_by"
        )

        widgets = {
            "state": forms.Select(attrs={"class": "form-select"}),
            "cpf_or_cnpj": forms.Select(
                attrs={"class": "form-select clients-form__cpf_or_cnpj"}
            ),
            "created_by_user": forms.Select(
                attrs={"class": "form-select"}
            )
        }
