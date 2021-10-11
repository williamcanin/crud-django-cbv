from django import forms
from .models import ClientModel


class ClientForm(forms.ModelForm):  # pragma: no cover
    class Meta:
        model = ClientModel
        fields = (
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
            "city"
        )

        widgets = {
            "state": forms.Select(attrs={"class": "form-select"}),
            "cpf_or_cnpj": forms.Select(
                attrs={"class": "form-select clients-form__cpf_or_cnpj"}
            )
        }
