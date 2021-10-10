import pytest
import re
from apps.clients.models import ClientModel

client_data = {
    "name": "William Canin",
    "email": "xpto@example.com",
    "birth_date": "1988-04-25",
    "district": "São Paulo",
    "state": "SP",
    "cpf_or_cnpj": "cpf",
    "cpf_cnpj": "123.456.789-00",
    "address": "Rua XYZ",
    "photo": "images/upload/default.jpg",
    "rg": "00.000.000-0",
    "cep": "16400-035",
    "cell_phone": "14000000000",
    "phone": "1400000000",
    "city": "São Paulo",
    "created_by_user": "william",
    "update_by": "william"
}


def test_ClientModel_str():

    obj = ClientModel(name="django")
    assert obj.__str__() == "django".title()


@pytest.mark.django_db
def test_ClientModel_cpf_cnpj():
    obj = ClientModel.objects.create(
        name=client_data["name"],
        email=client_data["email"],
        birth_date=client_data["birth_date"],
        district=client_data["district"],
        state=client_data["state"],
        cpf_or_cnpj=client_data["cpf_or_cnpj"],
        cpf_cnpj=client_data["cpf_cnpj"],
        address=client_data["address"],
        photo=client_data["photo"],
        rg=client_data["rg"],
        cep=client_data["cep"],
        cell_phone=client_data["cell_phone"],
        phone=client_data["phone"],
        city=client_data["city"],
        created_by_user=client_data["created_by_user"],
        update_by=client_data["update_by"]
    )
    obj.save()
    cpf_only_number = re.sub("[^0-9]", "", client_data["cpf_cnpj"])
    finder = ClientModel.objects.filter(cpf_cnpj=cpf_only_number)
    assert True if finder else False
