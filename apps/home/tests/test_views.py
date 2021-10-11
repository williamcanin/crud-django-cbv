import pytest
from django.test import RequestFactory
from apps.home.views import HomeView


@pytest.mark.django_db
def test_template_name_HomeView():
    request = RequestFactory().get("/")
    view = HomeView()
    view.setup(request)

    get_template_name = view.template_name
    assert get_template_name == "home/home.html"
