import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.db import transaction

from .models import User, Project, Audio, Text
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

    @transaction.atomic
    def create(self, validated_data):
        try: 
            user = self.context['request'].user
            project = Project.objects.create(
                project_title = validated_data['project_title'],
                user = user
            )
            audio = Audio.objects.create(
                speed = validated_data['speed'],
                project = project
            )

            bulk_list = []
            for text in validated_data['text']:
                bulk_list.append(Text(text=text, audio=audio))

            Text.objects.bulk_create(bulk_list)
            return project
        
        except Exception as e:
            transaction.set_rollback(rollback=True)
            raise ValidationError(str(e))


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
        """"page 별 10개의 문장까지 조회 가능"""
        page = int(self.context['request'].query_params['page'])
        page_size = 10
        limit = int(page_size * page)
        offset = int(limit - page_size)

        audio = Audio.objects.get(project=obj)
        texts = Text.objects.filter(audio=audio)[offset:limit]
        text = ' '.join(text.text for text in texts)
        return text

    def get_speed(self, obj):
        audio = Audio.objects.get(project=obj)
        return audio.speed

    def get_identifier(self, obj):
        audio = Audio.objects.get(project=obj)
        return audio.identifier