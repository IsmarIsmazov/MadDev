from django.db import models

from .constants import country_choices


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = 'Материалы'


class Chair(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    width = models.IntegerField(default=0, verbose_name="Ширина")
    height = models.IntegerField(default=0, verbose_name="Высота")
    depth = models.IntegerField(default=0, verbose_name="Глубина")
    material = models.ManyToManyField(Material, verbose_name="Материал")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    country = models.CharField(max_length=255, choices=country_choices, verbose_name="Страна")
    in_stock = models.BooleanField(verbose_name="В наличии")
    pickup = models.BooleanField(verbose_name="Самовывоз")
    delivery = models.BooleanField(verbose_name="Доставка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стул'
        verbose_name_plural = "Стулья"
