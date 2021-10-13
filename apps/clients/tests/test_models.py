import pytest
import re
from apps.clients.models import ClientModel


@pytest.fixture
@pytest.mark.django_db
def instance():
    data = ClientModel.objects.create(
        name_corporate="William Canin",
        email="xpto@example.com",
        birth_date="1988-04-25",
        district="São Paulo",
        state="SP",
        client_type="cpf",
        cpf_cnpj="123.456.789-00",
        complement_address="Rua XYZ",
        number_address="1478",
        photo="images/upload/default.jpg",
        rg="00.000.000-0",
        cep="16400-035",
        cell_phone="14000000000",
        phone="1400000000",
        city="São Paulo",
        obs="Cliente muito prestigiado.",
        created_by_user="william",
        update_by="william"
    )

    return data


def test_ClientModel_str():
    obj = ClientModel(name_corporate="django")
    assert obj.__str__() == "django".title()


@pytest.mark.django_db
def test_only_numbers(instance):
    instance.save()
    cpf_only_number = re.sub("[^0-9]", "", instance.cpf_cnpj)
    finder_cpf = ClientModel.objects.filter(cpf_cnpj=cpf_only_number)
    assert True if finder_cpf else False
    phone_only_number = re.sub("[^0-9]", "", instance.phone)
    finder_phone = ClientModel.objects.filter(phone=phone_only_number)
    assert True if finder_phone else False
    cell_phone_only_number = re.sub("[^0-9]", "", instance.cell_phone)
    finder_cell_phone = ClientModel.objects.filter(cell_phone=cell_phone_only_number)
    assert True if finder_cell_phone else False


@pytest.mark.django_db
def test_verify_photo_delete(instance):
    instance.save()
    instance.delete()
    assert True if not instance.photo.__str__() else False
