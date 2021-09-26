from django.contrib import admin
from .models import ClientModel


class ClientAdmin(admin.ModelAdmin):
    exclude = []
    # readonly_fields = ("cpf",)
    fieldsets = (
        ("Personal Data", {
            "fields": (
                ("name", "cpf"), ("city")
            ),
        }),
    )
    list_display = ("id", "name", "cpf", "city")
    search_fields = ("id", "name")


admin.site.register(ClientModel, ClientAdmin)
