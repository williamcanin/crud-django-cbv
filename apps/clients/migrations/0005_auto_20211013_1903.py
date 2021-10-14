# Generated by Django 3.2.8 on 2021-10-13 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_clientmodel_rg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmodel',
            name='name',
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='name_corporate',
            field=models.CharField(max_length=150, null=True, verbose_name='Nome/Razão Social'),
        ),
    ]