from django.contrib import admin
from .models import ClientModel
from django.contrib import messages


class ClientAdmin(admin.ModelAdmin):
    exclude = []
    # readonly_fields = ("cpf",)
    fieldsets = (
        ("Clients Data", {
            "fields": (
                ("created_by_user", "name", "email"), ("birth_date", "city", "district"),
                ("address", "cep", "rg"), ("cell_phone", "phone"), ("photo", "cpf_cnpj")
            ),
        }),
    )
    list_display = ("id", "name", "email", "address", "district",
                    "city", "cell_phone", "phone", "cpf_cnpj")
    search_fields = ("id", "name")

    def save_model(self, request, obj, form, change):
        obj.created_by_user = request.user
        messages.add_message(request, messages.SUCCESS, 'Salvado com sucesso.')
        return super().save_model(request, obj, form, change)


admin.site.register(ClientModel, ClientAdmin)
