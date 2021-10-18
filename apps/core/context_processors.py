from django.contrib.auth.models import User
from apps.users.models import UserCustom


def users_count(request):
    return {"users_count": UserCustom.objects.all().count()}
