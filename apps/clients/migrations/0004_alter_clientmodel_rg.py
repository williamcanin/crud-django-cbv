# Generated by Django 3.2.8 on 2021-10-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20211013_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='rg',
            field=models.CharField(blank=True, error_messages={'unique': 'Este RG já está registrado.'}, max_length=15, null=True, unique=True, verbose_name='RG'),
        ),
    ]
