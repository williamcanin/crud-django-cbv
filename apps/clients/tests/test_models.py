from apps.clients.models import ClientModel


def test_clientmodel_str():

    savior = ClientModel(name="jesus")
    assert savior.__str__() == "jesus".title()
