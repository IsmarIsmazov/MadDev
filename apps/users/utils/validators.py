from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator


class ValidateAuthenticate:
    @staticmethod
    def validate_password(value):
        if len(value) < 6 or len(value) > 20:
            raise ValidationError("Password must be between 6 and 20 characters long.")
        return value

    @staticmethod
    def validate_phone(value, queryset):
        if queryset.filter(phone_number=value).exists():
            raise ValidationError("Phone_number has already been used")
        return value


PhoneValidator = RegexValidator(regex=r"^996(\d{3})\d{2}\d{2}\d{2}$")
