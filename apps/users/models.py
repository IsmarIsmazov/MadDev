from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40)
    phone_number = PhoneNumberField(unique=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    object = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


class UserCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    time = models.DateTimeField()

    class Meta:
        verbose_name = "Код Верификации"
        verbose_name_plural = "Коды Верификации"

    def __str__(self):
        return f"{self.user}, {self.code}"
