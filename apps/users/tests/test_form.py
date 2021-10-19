import pytest
from django.urls import reverse_lazy
from django.test import Client
from django.contrib.auth.models import User
# from apps.users.forms import UserRegisterForm
# from apps.users.forms import UserCreationForm
from apps.users.models import UserCustom, UserManagerCustom

# from apps.users.views import SignUpView

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
    user = UserCustom.objects.create_user(email=data["username"], password=data["password1"])
    user.save()

    c = Client()
    response = c.post(
        reverse_lazy("sign-in"),
        {"username": data["username"], "password": data["password1"]},
    )
    assert response.status_code == 302


# @pytest.mark.django_db
# def test_auth_email():
#     user1 = {
#         "username": "william@gmail.com",
#         "first_name": "William",
#         "last_name": "Canin",
#         "email": "william@gmail.com",
#         "password1": "!Test123",
#         "password2": "!Test123",
#     }

#     user2 = {
#         "username": "william@gmail.com",
#         "first_name": "William",
#         "last_name": "Canin",
#         "email": "william@gmail.com",
#         "password1": "!Test123",
#         "password2": "!Test123",
#     }
#     UserCreationForm(user1).save()
#     get_user = UserCustom.objects.get(username=user1["username"])
#     assert get_user.has_perm("clients.view_clientmodel") is True
#     with pytest.raises(ValueError):
#         UserCreationForm(user2).save()
