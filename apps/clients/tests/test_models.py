import pytest
import re
from apps.clients.models import ClientModel


@pytest.fixture
@pytest.mark.django_db
def instance():
    data = ClientModel.objects.create(
        name="William Canin",
        email="xpto@example.com",
        birth_date="1988-04-25",
        district="São Paulo",
        state="SP",
        cpf_or_cnpj="cpf",
        cpf_cnpj="123.456.789-00",
        address="Rua XYZ",
        photo="images/upload/default.jpg",
        rg="00.000.000-0",
        cep="16400-035",
        cell_phone="14000000000",
        phone="1400000000",
        city="São Paulo",
        created_by_user="william",
        update_by="william"
    )

    return data


def test_ClientModel_str():
    obj = ClientModel(name="django")
    assert obj.__str__() == "django".title()


@pytest.mark.django_db
def test_only_numbers_cpf_cnpj(instance):
    instance.save()
    cpf_only_number = re.sub("[^0-9]", "", instance.cpf_cnpj)
    finder = ClientModel.objects.filter(cpf_cnpj=cpf_only_number)
    assert True if finder else False


@pytest.mark.django_db
def test_verify_photo_delete(instance):
    instance.save()
    instance.delete()
    assert True if not instance.photo.__str__() else False
