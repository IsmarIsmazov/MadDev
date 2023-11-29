from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from .models import Category, Chair, Material
from .serializers import ChairSerializer, CategorySerializer


# Create your views here.


class ChairViewSet(ModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer


class CategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


"""ВИДЫ КАТЕГОРИИ"""


# ------------------------------------------------------------------------------------------------------------------

class ChairOfficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Стулья офисные')
    serializer_class = ChairSerializer


class ArmchairOfficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Кресла офисные')
    serializer_class = ChairSerializer


class TableOfficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Столы офисные')
    serializer_class = ChairSerializer


class ClosetOfficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Шкафы офисные')
    serializer_class = ChairSerializer


class ArmchairGameViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Игровые кресла')
    serializer_class = ChairSerializer


class ExecutiveArmchairViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Руководит-е кресла')
    serializer_class = ChairSerializer


class ChildrenArmchairViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Детские кресла')
    serializer_class = ChairSerializer


class PartsChairViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Chair.objects.filter(category__name='Стулья офисные')
    serializer_class = ChairSerializer


"""КОНЕЦ ВИДЫ КАТЕГОРИИ"""

# ------------------------------------------------------------------------------------------------------------------
