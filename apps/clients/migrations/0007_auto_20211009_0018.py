# Generated by Django 3.2.7 on 2021-10-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20211008_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='created_by_user',
            field=models.CharField(max_length=30, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='update_by',
            field=models.CharField(max_length=30, verbose_name='Ultima atualização por'),
        ),
    ]