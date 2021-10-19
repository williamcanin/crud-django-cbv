from django import forms
from .models import ClientModel
from crispy_forms.helper import FormHelper


class ClientForm(forms.ModelForm):  # pragma: no coverage
    class Meta:
        model = ClientModel
        fields = (
            "photo",
            "client_type",
            "cpf_cnpj",
            "name_corporate",
            "email",
            "birth_date",
            "district",
            "state",
            "address",
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
            "birth_date": forms.TextInput(attrs={"type": "date"}),
            "email": forms.TextInput(attrs={"placeholder": "my-email@example.com"}),
            "cpf_cnpj": forms.TextInput(attrs={"class": "clients-form__input-cpf-cnpj"}),
            "cell_phone": forms.TextInput(attrs={"data-mask": "(00) 00000-0000", "placeholder": "(00) 00000-0000"}),
            "phone": forms.TextInput(attrs={"data-mask": "(00) 0000-0000", "placeholder": "(00) 0000-0000"}),
            "obs": forms.Textarea(attrs={"placeholder": "Escreva uma observação para este Cliente"}),
            "name_corporate": forms.TextInput(attrs={"placeholder": "Ex: Elvis Presley"}),
            "rg": forms.TextInput(attrs={"placeholder": "Ex: 99.999.999-9"}),
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if user.cpf_cnpj == self.cleaned_data["cpf_cnpj"]:
    #         return ValueError("Dado existe")
    #     if commit:
    #         user.save()
    #     return user
