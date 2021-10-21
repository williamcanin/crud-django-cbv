# Comment out all this code if you don't want to use custom.
# The custom uses email for login instead of user.

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManagerCustom(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("E-mail é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ser 'is_superuser=True'.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ser 'is_staff=True'.")
        return self._create_user(email, password, **extra_fields)


class UserCustom(AbstractUser):
    email = models.EmailField("E-mail", unique=True)
    first_name = models.CharField(
        "Primeiro nome", max_length=100, error_messages={"required": "Not null"}
    )
    last_name = models.CharField(
        "Ultimo nome", max_length=100, error_messages={"required": "Not null"}
    )
    # cell_phone = models.CharField('Celular', max_length=18)
    is_staff = models.BooleanField("Membro", default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    objects = UserManagerCustom()
