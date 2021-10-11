from django.contrib.auth.models import User


def users_count(request) -> int:
    return {"users_count": User.objects.all().count()}
