from django.db import models
from apps.chairs.models import Chair
from apps.users.models import CustomUser


# Create your models here.


class Favorite(models.Model):
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE, verbose_name="Продукт для избранных")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
