import pytest
from django.urls import reverse_lazy
from django.test import Client
from django.contrib.auth.models import User
from apps.users.forms import UserRegisterForm
from apps.users.views import SignUpView


def test_user_not_auth():
    assert Client().get(reverse_lazy('client_read')).status_code == 302
    assert Client().get(reverse_lazy('client_new')).status_code == 302


@pytest.mark.django_db
def test_auth_user():
    data = {
        "username": "williamcanin",
        "first_name": "William",
        "last_name": "Canin",
        "email": "william.costa.canin_x@gmail.com",
        "password1": "!Test123",
        "password2": "!Test123"
    }
    user1 = UserRegisterForm(data)
    user1.save()

    c = Client()
    response = c.post(reverse_lazy('sign-in'), {'username': data['username'], 'password': data['password1']})
    assert response.url == "/"
    assert response.status_code == 302


@pytest.mark.django_db
def test_auth_email():
    user1 = {
        "username": "williamcanin",
        "first_name": "William",
        "last_name": "Canin",
        "email": "william@gmail.com",
        "password1": "!Test123",
        "password2": "!Test123"
    }

    user2 = {
        "username": "williamcanin2",
        "first_name": "William",
        "last_name": "Canin",
        "email": "william@gmail.com",
        "password1": "!Test123",
        "password2": "!Test123"
    }
    UserRegisterForm(user1).save()
    get_user = User.objects.get(username=user1["username"])
    assert get_user.has_perm('clients.view_clientmodel') is True
    with pytest.raises(ValueError):
        UserRegisterForm(user2).save()
