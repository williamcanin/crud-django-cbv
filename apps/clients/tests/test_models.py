import re
from apps.clients.models import ClientModel


def test_ClientModel_str():

    obj = ClientModel(name="django")
    assert obj.__str__() == "django".title()


def test_ClientModel_cpf_cnpj():
    pass
