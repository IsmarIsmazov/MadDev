from django.contrib.auth import authenticate, login
from django.utils import timezone
from rest_framework import status, viewsets, response, exceptions
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser, UserCode
from rest_framework.response import Response

from apps.users.utils.tokens import create_jwt_pair_for_user
from . import utils
from .utils import generate_verification_code


class Authenticate:

    # ----------Register----------------------------------------------------------------------------------------------------
    @staticmethod
    def create_user(serializer, request):
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # --------------LOGIN------------------------------------------------------------------------------------
    @staticmethod
    def login_user(serializer):
        user = authenticate(
            phone_number=serializer.validated_data["phone_number"],
            password=serializer.validated_data["password"]
        )

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successful", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"message": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class PostOnlyViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                 data={"error": "METHOD NOT ALLOWED"})

    def update(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                 data={"error": "METHOD NOT ALLOWED"})

    def destroy(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                 data={"error": "METHOD NOT ALLOWED"})

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                                 data={"error": "METHOD NOT ALLOWED"})


class GetLoginResponseService:
    @staticmethod
    def get_jwt(user):
        refresh = RefreshToken.for_user(user)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data


class UserServices:
    __user_model = CustomUser
    __user_code_model = UserCode

    @classmethod
    def user_password_reset_search_user_service(cls, serializer):
        serializer.is_valid(raise_exception=True)
        try:
            phone_number = serializer.validated_data["phone_number"]
            user = cls.__user_model.objects.get(phone_number=phone_number)
            code = generate_verification_code()
            time = timezone.now() + timezone.timedelta(minutes=10)

            password_reset_token = cls.__user_code_model(user=user, code=code, time=time)
            password_reset_token.save()
            utils.send_to_the_code_phone(phone_number, code)

            return {"code": code}

        except cls.__user_model.DoesNotExist:
            return {"error": "Not Found"}

    @classmethod
    def user_registration_service(cls, serializer):
        serializer.is_valid(raise_exception=True)
        user = cls.__user_model.objects.create_user(**serializer.validated_data)

        # генерация кода для логина
        activate_code = generate_verification_code()
        time = timezone.now() + timezone.timedelta(minutes=10)

        # Сохранение токена в базе данных
        code = cls.__user_code_model.objects.create(user_id=user.id, code=activate_code, time=time)
        code.save()
        utils.send_to_the_code_phone(
            serializer.validated_data["phone_number"], activate_code
        )
        return {"message": "sended",
                "code": f"{activate_code}",
                "user_id": user.id}

    @classmethod
    def user_confirm_service(cls, serializer):
        code = cls.__user_code_model.objects.filter(code=serializer.validated_data["code"])
        if code:
            cls.__user_model.objects.update(is_active=True)
            cls.__user_code_model.objects.filter(
                code=serializer.validated_data["code"]
            ).delete()
            return {"message": "confirmed"}

        return {"error": "wrong id or code"}

    @classmethod
    def user_password_reset_token_service(cls, serializer):
        try:
            code = serializer.validated_data["code"]
            user_code = cls.__user_code_model.objects.get(
                code=code, time__gt=timezone.now()
            )
            return {"message": "ok", "code": code}

        except cls.__user_code_model.DoesNotExist:
            return {"error": "Not found"}

    @classmethod
    def user_password_reset_new_password(cls, serializer, **kwargs):
        try:
            password_reset_token = UserCode.objects.get(
                code=kwargs["code"], time__gt=timezone.now()
            )
        except cls.__user_code_model.DoesNotExist:
            return {"error": "Not Found"}

        serializer.is_valid(raise_exception=True)

        user = password_reset_token.user
        password = serializer.validated_data["password"]

        user.set_password(password)
        user.save()

        password_reset_token.delete()

        return {"message": "success"}

    @classmethod
    def user_login_service(cls, request, serializer, **kwargs):
        password_reset_token = cls.__user_code_model.objects.get(
            token=kwargs["code"], time__gt=timezone.now())
        serializer.is_valid(raise_exception=True)
        user = authenticate(request=request, **serializer.validated_data)
        if not user:
            raise exceptions.AuthenticationFailed
        login(request, user)
        password_reset_token.delete()
        return {"id": user.id,
                "detail": GetLoginResponseService.get_jwt(user=user)
                }


