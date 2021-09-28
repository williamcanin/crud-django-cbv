from django.contrib import admin
from .models import ClientModel


class ClientAdmin(admin.ModelAdmin):
    exclude = []
    # readonly_fields = ("cpf",)
    fieldsets = (
        ("Clients Data", {
            "fields": (
                ("name", "email"), ("birth_date", "city", "district"),
                ("address", "cep", "rg"), ("cell_phone", "phone"), ("photo", "cpf_cnpj")
            ),
        }),
    )
    list_display = ("id", "name", "email", "address", "district",
                    "city", "cell_phone", "phone", "cpf_cnpj")
    search_fields = ("id", "name")


admin.site.register(ClientModel, ClientAdmin)
