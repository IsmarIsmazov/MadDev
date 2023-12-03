from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status, response, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import CustomUser
from apps.users.serializers import SignUpSerializer, LoginSerializer
from apps.users.utils.permissions import IsUnregistered
from apps.users.utils.service import Authenticate, UserServices


# Create your views here.
class SignUpView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsUnregistered]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            register = UserServices.user_registration_service(serializer)
            return response.Response(data=register)

        except IntegrityError:
            return response.Response(
                data={"detail": "Already Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [IsUnregistered]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Authenticate.login_user(serializer)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
