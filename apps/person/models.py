import re
from django.db import models
from contextlib import suppress


class PersonModel(models.Model):
    objects = None
    name = models.CharField('Nome', max_length=150, null=True)
    cpf = models.CharField('CPF', max_length=15, null=True,)
    photo = models.ImageField('Imagem',
                              default="default.png",
                              upload_to="images/upload", null=True, blank=True
                              )
    city = models.CharField('Cidade', max_length=80, null=True)
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Data de atualização', auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}".title()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["id"]

    def save(self, *args, **kwargs):

        # Remove hyphen and dot of SSA before save
        self.cpf = re.sub("[^0-9]", "", self.cpf)

        # Remove old photo after adding new
        with suppress(Exception):
            obj = PersonModel.objects.get(id=self.id)
            if obj.photo != self.photo and obj.photo != "default.png":
                obj.photo.delete(save=False)

        # Save
        super(PersonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # Before deleting the record, remove the photo for the record
        self.photo.delete()
        super(PersonModel, self).delete(*args, **kwargs)
