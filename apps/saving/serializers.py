from rest_framework import serializers
from apps.chairs.serializers import ChairSerializer
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ('chair', 'user')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation_chair = {
            'name_chair': instance.chair.title
        }
        representation['user'] = instance.user.username
        representation.update(representation_chair)
        return representation
