from django.contrib import admin
from .models import PersonModel


class PersonAdmin(admin.ModelAdmin):
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


admin.site.register(PersonModel, PersonAdmin)
