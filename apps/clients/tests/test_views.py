from apps.clients.views import is_validate


def test_is_validate():
    field = "William"
    data = is_validate(field)
    assert True if data else False
    field = ""
    data = is_validate(field)
    assert True if not data else False
