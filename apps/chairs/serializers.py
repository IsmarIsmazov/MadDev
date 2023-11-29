from rest_framework import serializers

from .models import Chair, Category, Material


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class ChairSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Chair
        fields = "__all__"
