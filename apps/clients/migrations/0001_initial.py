# Generated by Django 3.2.7 on 2021-10-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('district', models.CharField(max_length=150, null=True, verbose_name='Bairro')),
                ('state', models.CharField(choices=[('default', 'Selecione um estado'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraiba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], default='default', max_length=25, verbose_name='Estados')),
                ('cpf_or_cnpj', models.CharField(choices=[('cpf', 'CPF'), ('cnpj', 'CNPJ')], default='cpf', max_length=10, verbose_name='CPF/CNPJ')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=18, verbose_name='CPF/CNPJ')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='Endereço')),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='images/upload', verbose_name='Imagem')),
                ('rg', models.CharField(max_length=15, null=True, verbose_name='RG')),
                ('cep', models.CharField(max_length=15, null=True, verbose_name='CEP')),
                ('cell_phone', models.CharField(max_length=15, null=True, verbose_name='CEL')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Fone')),
                ('city', models.CharField(max_length=80, null=True, verbose_name='Cidade')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'tbl_clients',
                'ordering': ['id'],
            },
        ),
    ]