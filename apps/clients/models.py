import re
from django.db import models
from contextlib import suppress


class ClientModel(models.Model):
    objects = None
    name = models.CharField('Nome', max_length=150, null=True)
    email = models.EmailField(max_length=254, blank=True)
    birth_date = models.DateField('Data de Nascimento', null=True)
    district = models.CharField('Bairro', max_length=150, null=True)
    # state = models.CharField('Estado', max_length=80, null=True)
    address = models.CharField('Endereço', max_length=250, null=True)
    photo = models.ImageField('Imagem',
                              default="default.png",
                              upload_to="images/upload", null=True, blank=True
                              )
    cpf = models.CharField('CPF', max_length=15, null=True)
    rg = models.CharField('RG', max_length=15, null=True)
    cep = models.CharField('CEP', max_length=15, null=True)
    cnpj = models.CharField('CNPJ', max_length=16, blank=True)
    cell_phone = models.CharField('CEL', max_length=15, null=True)
    phone = models.CharField('Fone', max_length=15, blank=True)
    city = models.CharField('Cidade', max_length=80, null=True)
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Data de atualização', auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}".title()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["id"]

    def save(self, *args, **kwargs):

        # Remove hyphen and dot of CPF before save
        self.cpf = re.sub("[^0-9]", "", self.cpf)

        # Remove hyphen and dot of CNPJ before save
        self.cnpj = re.sub("[^0-9]", "", self.cnpj)

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
