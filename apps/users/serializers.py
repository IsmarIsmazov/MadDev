from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser
from .utils.validators import ValidateAuthenticate


class SignUpSerializer(ModelSerializer):

    def validate_password(self, value):
        return ValidateAuthenticate.validate_password(value)

    def validate_phone(self, value):
        queryset = CustomUser.objects.all()
        return ValidateAuthenticate.validate_phone(value, queryset)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password', 'refresh_token', 'access_token']
        extra_kwargs = {'password': {'write_only': True},
                        'refresh_token': {'read_only': True},
                        'access_token': {'read_only': True}}
