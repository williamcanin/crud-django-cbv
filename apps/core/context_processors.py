from django.contrib.auth.models import User


def users_count(request):
    return {"users_count": User.objects.all().count()}
