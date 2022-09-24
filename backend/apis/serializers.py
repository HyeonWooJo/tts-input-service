import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Project, Audio
from core.utils import text_validation


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
    text = serializers.CharField(write_only=True)
    speed = serializers.FloatField(write_only=True)

    class Meta:
        model = Project
        fields = [
            'project_title',
            'text',
            'speed',
        ]

    def validate_text(self, text):
        value = text_validation(text)
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        project = Project.objects.create(
            project_title = validated_data['project_title'],
            user = user
        )
        audio = Audio.objects.create(
            text = validated_data['text'],
            speed = validated_data['speed'],
            project = project
        )
        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    """프로젝트 디테일 Serializer"""
    text = serializers.SerializerMethodField()
    speed = serializers.SerializerMethodField()
    identifier = serializers.SerializerMethodField()
    

    class Meta:
        model = Project
        fields = [
            'project_title',
            'text',
            'speed',
            'identifier'
        ]

    def get_text(self, obj):
        audio = Audio.objects.get(id=obj.id)
        return audio.text

    def get_speed(self, obj):
        audio = Audio.objects.get(id=obj.id)
        return audio.speed

    def get_identifier(self, obj):
        audio = Audio.objects.get(id=obj.id)
        return audio.identifier