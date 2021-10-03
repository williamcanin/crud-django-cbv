from django.contrib.auth.models import User


def users_count(request):
    return {"total_user": User.objects.all().count()}
