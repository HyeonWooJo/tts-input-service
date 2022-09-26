from re import L
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    "유저 매니저 정의"
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("계정 이름을 입력해주세요.")
        if not password:
            raise ValueError("비밀번호를 입력해주세요.")
        if not email:
            raise ValueError("이메일을 입력해주세요.")

        user = self.model(
            username = username,
            password = password,
            email = email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            password = password,
            email = email
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    """유저 모델"""
    username = models.CharField(verbose_name="ID", max_length=20, unique=True)
    email = models.CharField(verbose_name="E-mail", max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    # status
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        db_table = "users"


class Project(models.Model):
    """프로젝트 모델"""
    project_title = models.CharField(verbose_name="프로젝트 이름", max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "projects"


class Audio(models.Model):
    """오디오 모델"""
    audio_file = models.FileField(null=True)
    speed = models.FloatField(verbose_name="스피드", max_length=10)
    identifier = models.UUIDField( 
        default=uuid.uuid4,
        unique=True,
        editable=False
        )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "audios"


class Text(models.Model):
    """텍스트 모델"""
    text = models.CharField(verbose_name="텍스트", max_length=300)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)

    class Meta:
        db_table = "texts"