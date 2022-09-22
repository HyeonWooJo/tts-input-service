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

from .serializers import SignupSerializer, SignInSerializer


class SignupAPIView(CreateAPIView):
    """
    회원가입 API
    :endpoint: /api/signup
    :return: id
            username
            email
    """
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SigninAPIView(CreateAPIView):
    """
    로그인 API
    :endpoint: /api/signin
    :return: 로그인 성공여부
            access token
            refresh token
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class DeleteUserView(DestroyAPIView):
    """
    계정 삭제 API
    :endpoint: /api/users/delete/<int>
    :return: 없음
    """
    queryset = get_user_model().objects.all()