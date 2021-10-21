import pytest
from apps.core.context_processors import users_count


@pytest.mark.django_db
def test_users_count(request):
    dict_ = users_count(request)
    assert type(dict_["users_count"]) is int
