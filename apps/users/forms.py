# from django import forms
from django.contrib.auth.models import Permission
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from contextlib import suppress
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import UserCustom
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.layout import Column, Row, ButtonHolder


class AuthenticationFormCustom(AuthenticationForm):
    # __init__ Django Crispy
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column("username", css_class="mb-3"),
                Column("password", css_class="mb-3"),
                ButtonHolder(
                    Submit('submit', 'Entrar', css_class='btn btn-primary w-100'),
                )
            )
        )


class UserCreationFormCustom(UserCreationForm):
    PERM_VIEWS = [
        "Can view Client",
    ]

    class Meta:
        model = UserCustom
        fields = ["username", "first_name", "last_name"]
        labels = {"username": "E-Mail"}

    # __init__ Django Crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Row(
                Column("username", css_class="mb-3"),
                Column("first_name", css_class="mb-3"),
                Column("last_name", css_class="mb-3"),
                Column("password1", css_class="mb-3"),
                Column("password2", css_class="mb-3"),
                ButtonHolder(
                    Submit('submit', 'Entrar', css_class='btn btn-primary w-100'),
                )
            )
        )

    # def clean_email(self):
    #     get_email = self.cleaned_data["username"]
    #     if UserCustom.objects.filter(email=get_email).exists():
    #         raise ValidationError(f"O email {get_email} já está em uso.")
    #     return get_email

    def save(self, commit=True):
        user = super().save(commit=False)
        # Assign password
        user.set_password(self.cleaned_data["password1"])
        # Save datas in Capitalize
        user.first_name = self.cleaned_data["first_name"].title()
        user.last_name = self.cleaned_data["last_name"].title()
        # Save data in lower text
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()

            # Add permissions to here user
            if self.PERM_VIEWS:
                for perm in self.PERM_VIEWS:
                    with suppress(Exception):
                        permission = Permission.objects.get(name=perm)
                        user.user_permissions.add(permission)

            # Add user to group "read_only"
            # with suppress(Exception):
            # read_only = Group.objects.get(name='read_only')
            # user.groups.add(read_only)

        return user


class UserChangeFormCustom(UserChangeForm):
    class Meta:
        model = UserCustom
        fields = {'first_name', 'last_name'}


# # Not customized
# class UserRegisterForm(UserCreationForm):
#     PERM_VIEWS = [
#         "Can view Client",
#     ]
#     email = forms.EmailField(max_length=100)

#     class Meta:
#         model = User
#         fields = ["username", "email", "first_name", "last_name"]

#     # Validar email se existe
#     def clean_email(self):
#         get_email = self.cleaned_data["email"]
#         if User.objects.filter(email=get_email).exists():
#             raise ValidationError(f"O email {get_email} já está em uso.")
#         return get_email

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         # Save datas in Capitalize
#         user.first_name = self.cleaned_data["first_name"].title()
#         user.last_name = self.cleaned_data["last_name"].title()
#         # Save data in lower text
#         user.email = self.cleaned_data["email"].lower()
#         # Assign password
#         user.set_password(self.cleaned_data["password1"])

#         if commit:
#             user.save()

#             # Add permissions to here user
#             if self.PERM_VIEWS:
#                 for perm in self.PERM_VIEWS:
#                     with suppress(Exception):
#                         permission = Permission.objects.get(name=perm)
#                         user.user_permissions.add(permission)

#             # Add user to group "read_only"
#             # with suppress(Exception):
#             # read_only = Group.objects.get(name='read_only')
#             # user.groups.add(read_only)

#         return user
