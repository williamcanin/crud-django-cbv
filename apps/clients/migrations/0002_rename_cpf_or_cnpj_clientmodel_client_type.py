# Generated by Django 3.2.8 on 2021-10-13 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientmodel',
            old_name='cpf_or_cnpj',
            new_name='client_type',
        ),
    ]
