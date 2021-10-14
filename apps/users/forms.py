from django import forms
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm
from contextlib import suppress
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):  # pragma: no coverage
    PERM_VIEWS = [
        "Can view Client",
    ]
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    # Validar email se existe
    def clean_email(self):
        get_email = self.cleaned_data["email"]
        if User.objects.filter(email=get_email).exists():
            raise ValidationError(f"O email {get_email} já está em uso.")
        return get_email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

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
