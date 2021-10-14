from django.contrib import admin
from .models import ClientModel
from django.contrib import messages


class ClientAdmin(admin.ModelAdmin):
    exclude = []
    readonly_fields = ("created_by_user", "update_by")
    fieldsets = (
        (
            "Clients Data",
            {
                "fields": (
                    ("name_corporate", "email"),
                    ("birth_date", "city", "district"),
                    ("address", "complement_address", "number_address"),
                    ("cep", "rg", "cell_phone"),
                    ("phone", "photo", "cpf_cnpj"),
                    ("created_by_user", "update_by"),
                ),
            },
        ),
    )
    list_display = (
        "id",
        "name_corporate",
        "email",
        "address",
        "number_address",
        "complement_address",
        "district",
        "city",
        "cell_phone",
        "phone",
        "cpf_cnpj",
    )
    search_fields = ("id", "name_corporate")

    def save_model(self, request, obj, form, change):
        # Modifica apenas na criação
        if not change:
            obj.created_by_user = request.user.username

        # Modifica na atualização e criação
        obj.update_by = request.user.username
        messages.add_message(request, messages.SUCCESS, "Salvado com sucesso.")
        return super().save_model(request, obj, form, change)


admin.site.register(ClientModel, ClientAdmin)
