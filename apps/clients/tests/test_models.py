import pytest
import re
from apps.clients.models import ClientModel


class TestClient():
    CLIENT_DATA = {
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

    def test_ClientModel_str(self):
        obj = ClientModel(name="django")
        assert obj.__str__() == "django".title()

    @pytest.mark.django_db
    def test_ClientModel_cpf_cnpj(self):
        obj = ClientModel.objects.create(
            name=self.CLIENT_DATA["name"],
            email=self.CLIENT_DATA["email"],
            birth_date=self.CLIENT_DATA["birth_date"],
            district=self.CLIENT_DATA["district"],
            state=self.CLIENT_DATA["state"],
            cpf_or_cnpj=self.CLIENT_DATA["cpf_or_cnpj"],
            cpf_cnpj=self.CLIENT_DATA["cpf_cnpj"],
            address=self.CLIENT_DATA["address"],
            photo=self.CLIENT_DATA["photo"],
            rg=self.CLIENT_DATA["rg"],
            cep=self.CLIENT_DATA["cep"],
            cell_phone=self.CLIENT_DATA["cell_phone"],
            phone=self.CLIENT_DATA["phone"],
            city=self.CLIENT_DATA["city"],
            created_by_user=self.CLIENT_DATA["created_by_user"],
            update_by=self.CLIENT_DATA["update_by"]
        )
        obj.save()
        cpf_only_number = re.sub("[^0-9]", "", self.CLIENT_DATA["cpf_cnpj"])
        finder = ClientModel.objects.filter(cpf_cnpj=cpf_only_number)
        assert True if finder else False
