from django import forms
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.forms import UserCreationForm
# from contextlib import suppress


class UserRegisterForm(UserCreationForm):
    PERM_VIEWS = [
        'Can view Client',
    ]
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            # Add permissions to here user
            if self.PERM_VIEWS:
                for perm in self.PERM_VIEWS:
                    permission = Permission.objects.get(name=perm)
                    user.user_permissions.add(permission)

            # Add user to group "read_only"
            # with suppress(Exception):
                # read_only = Group.objects.get(name='read_only')
                # user.groups.add(read_only)

        return user
