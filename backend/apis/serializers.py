import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Project, Audio


class SignupSerializer(serializers.ModelSerializer):
    """회원가입 Serializer"""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'username',
            'email',
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class SignInSerializer(TokenObtainPairSerializer):
    """로그인 Serializer"""
    def validate(self, data):
        """로그인 유효성 검사"""
        username = data.get("username")
        password = data.get("password")

        user = User.objects.get(username=username)

        if user:
            if not user.is_active:
                raise serializers.ValidationError("비활성화된 계정입니다.")

            if not user.check_password(password):
                raise serializers.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")
        else:
            raise serializers.ValidationError("아이디 또는 비빌먼호를 잘못 입력했습니다.")

        token = super().get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)

        data = {
            "access" : access_token,
            "refresh" : refresh_token,
        }
        return data


class ProjectSerializer(serializers.ModelSerializer):
    """프로젝트 Serializer"""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = Audio
        fields = [
            'text'
        ]

    def validate_text(self, text):
        """텍스트 유효성 검사"""

        """빈 문자열 제거"""
        if not text:
            ValidationError('문자열이 비어있습니다.') 
        
        text = text[0]
        
        """텍스트에 한글, 영어, 숫자, 물음표, 느낌표, 마침표, 따옴표, 공백 외 다른 문자열 제거"""
        REGEX_TEXT = '^[a-zA-Z가-힣0-9.,?!\"\'\s]'
        text = re.sub(REGEX_TEXT, '', text)

        """맨 앞과 뒤 공백 제거"""
        text = text.strip()

        """.과 ?과 !를 구분자로 텍스트 쪼개기"""
        text = re.split('([.|?|!])', text)

        for i in range(len(text)):
            if text[i] in ('.', '?', '!'):
                text[i] += '*'

        text = ''.join(text)
        text = re.split('[*]', text)

        value = []

        for i in range(len(text)):
            if len(text[i]) > 1:
                value.append(text[i])

        return value