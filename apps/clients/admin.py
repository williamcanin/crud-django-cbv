from django.contrib import admin
from .models import ClientModel


class ClientAdmin(admin.ModelAdmin):
    exclude = []
    # readonly_fields = ("cpf",)
    fieldsets = (
        ("Clients Data", {
            "fields": (
                ("name", "email", "cpf"), ("birth_date", "city", "district"),
                ("address", "cep", "rg"), ("cell_phone", "cnpj", "phone"), ("photo")
            ),
        }),
    )
    list_display = ("id", "name", "cpf", "cnpj", "email", "address", "district",
                    "city", "cell_phone", "phone")
    search_fields = ("id", "name")


admin.site.register(ClientModel, ClientAdmin)
