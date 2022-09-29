from django.contrib import admin
from .models import *


"""어드민 유저 관리"""
admin.site.register(User)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """어드민 프로젝트 관리"""
    list_display = ['id','project_title','user','created_at','updated_at']
    list_display_links = ['id']
    search_fields = ['id']

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    """어드민 오디오 관리"""
    list_display = ['id','project','identifier','speed','audio_file']
    list_display_links = ['id']
    search_fields = ['id']
    list_filter = ['id', 'project']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    """어드민 텍스트 관리"""
    list_display = ['id','idx', 'audio','text']
    list_display_links = ['id']
    search_fields = ['id']
    list_filter = ['id']
