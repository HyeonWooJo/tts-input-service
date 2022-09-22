from django.db import models


class TimeStampModel(models.Model):
    """유저 모델"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstact = True