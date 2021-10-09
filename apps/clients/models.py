import re
from django.db import models
from contextlib import suppress

# from django.conf import settings
# from django.contrib.auth.models import User
from apps.core.places import STATES_BRAZIL


CHOICE_CPF_CNPJ = (("cpf", "CPF"), ("cnpj", "CNPJ"))


class ClientModel(models.Model):
    # objects = None
    # created_by_user = models.ForeignKey(
    #     User, on_delete=models.DO_NOTHING,
    #     related_name="created_by", default=User, blank=True
    # )
    name = models.CharField("Nome", max_length=150, null=True)
    email = models.EmailField(
        max_length=254,
        unique=True,
        error_messages={"unique": "Este e-mail já está registrado."},
    )
    birth_date = models.DateField("Data de Nascimento", null=True)
    district = models.CharField("Bairro", max_length=150, null=True)
    state = models.CharField(
        "Estados", max_length=25, choices=STATES_BRAZIL, default="default"
    )
    cpf_or_cnpj = models.CharField(
        "CPF/CNPJ", max_length=10, choices=CHOICE_CPF_CNPJ, default="cpf"
    )
    cpf_cnpj = models.CharField(
        "CPF/CNPJ",
        max_length=18,
        unique=True,
        error_messages={"unique": "Este CPF/CNPF já está registrado."},
    )
    address = models.CharField("Endereço", max_length=250, null=True)
    photo = models.ImageField(
        "Imagem",
        default="default.png",
        upload_to="images/upload",
        null=True,
        blank=True,
    )
    rg = models.CharField(
        "RG",
        max_length=15,
        unique=True,
        error_messages={"unique": "Este RG já está registrado."},
    )
    cep = models.CharField("CEP", max_length=15, null=True)
    cell_phone = models.CharField("CEL", max_length=15, null=True)
    phone = models.CharField("Fone", max_length=15, blank=True)
    city = models.CharField("Cidade", max_length=80, null=True)
    created_by_user = models.CharField("Criado por", max_length=30)
    update_by = models.CharField("Ultima atualização por", max_length=30)
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True, null=True)
    update_at = models.DateTimeField("Data de atualização", auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}".title()

    class Meta:
        db_table = "tbl_clients"
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["id"]

    def save(self, *args, **kwargs):

        # Remove hyphen and dot of CPF/CNPJ before save
        self.cpf_cnpj = re.sub("[^0-9]", "", self.cpf_cnpj)

        # Remove hyphen and dot of PHONE before save
        self.phone = re.sub("[^0-9]", "", self.phone)

        # Remove hyphen and dot of CELL PHONE before save
        self.cell_phone = re.sub("[^0-9]", "", self.cell_phone)

        # Remove old photo after adding new
        with suppress(Exception):
            obj = ClientModel.objects.get(id=self.id)
            if obj.photo != self.photo and obj.photo != "default.png":
                obj.photo.delete(save=False)
        # Save
        super(ClientModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # Before deleting the record, remove the photo for the record
        self.photo.delete()
        super(ClientModel, self).delete(*args, **kwargs)
