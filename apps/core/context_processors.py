# from django.contrib.auth.models import User
from apps.users.models import UserCustom
from django.utils import translation


def users_count(request):
    return {"users_count": UserCustom.objects.all().count()}


def get_lang_browser(request):
    return {"lang": translation.get_language()}
