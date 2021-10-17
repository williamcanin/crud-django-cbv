from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeFormCustom, UserCreationFormCustom
from .models import UserCustom


@admin.register(UserCustom)
class UserAdminCustom(UserAdmin):
    add_form = UserCreationFormCustom
    form = UserChangeFormCustom
    model = UserCustom
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("first_name", "last_name")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Datas importantes", {"fields": ("last_login", "date_joined")}),
    )
