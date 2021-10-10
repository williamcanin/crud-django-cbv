from apps.clients.models import ClientModel


def test_clientmodel_str():

    client1 = ClientModel(name="jesus")
    assert client1.__str__() == "jesus".title()
