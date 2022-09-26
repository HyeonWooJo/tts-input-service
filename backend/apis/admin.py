from django.contrib import admin
from .models import *

admin.site.register(User)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','project_title','user','created_at','updated_at']


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['id','project','identifier','speed','audio_file']


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id','idx', 'audio','text']