from django import forms
from .models import ClientModel


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
            "rg",
            "cep",
            "complement_address",
            "number_address",
            "cell_phone",
            "phone",
            "city",
            "obs"
        )

        widgets = {
            "state": forms.Select(attrs={"class": "form-select clients-form__states"}),
            "client_type": forms.Select(
                attrs={"class": "form-select clients-form__client_type"}
            )
        }
