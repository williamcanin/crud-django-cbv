# Generated by Django 3.2.7 on 2021-10-09 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_clientmodel_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='cell_phone',
            field=models.CharField(default=1, max_length=15, unique=True, verbose_name='CEL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='cpf_cnpj',
            field=models.CharField(max_length=18, unique=True, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='rg',
            field=models.CharField(default=1, max_length=15, unique=True, verbose_name='RG'),
            preserve_default=False,
        ),
    ]
