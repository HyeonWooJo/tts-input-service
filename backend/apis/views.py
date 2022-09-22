from django.contrib.auth import get_user_model
from django.http import HttpResponse

from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SignupSerializer


class SignupAPIView(CreateAPIView):
    """
    회원가입 API
    :endpoint: /api/users/signup
    :return: id
            username
            email
    """
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)