import pytest
from django.urls import reverse_lazy
from django.test import Client
from apps.users.models import UserCustom
from django.db import IntegrityError


@pytest.mark.django_db
def test_user_not_auth():
    assert Client().get(reverse_lazy("client_read")).status_code == 302
    assert Client().get(reverse_lazy("client_new")).status_code == 302


@pytest.mark.django_db
def test_auth_user():
    data = {
        "username": "william.costa.canin@gmail.com",
        "password1": "!Test123",
        "password2": "!Test123",
    }
    user1 = UserCustom.objects.create_user(
        email=data["username"], password=data["password1"]
    )
    user1.save()

    c = Client()
    response = c.post(
        reverse_lazy("sign-in"),
        {"username": data["username"], "password": data["password1"]},
    )
    assert response.status_code == 302

    with pytest.raises(IntegrityError):
        user2 = UserCustom.objects.create_user(
            email=data["username"], password=data["password1"]
        )
        user2.save()
