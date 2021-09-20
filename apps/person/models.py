from django.db import models


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
