from django.contrib import admin
from .models import *

admin.site.register(User)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','project_title','user','created_at','updated_at']
    list_display_links = ['id']
    search_fields = ['id']

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['id','project','identifier','speed','audio_file']
    list_display_links = ['id']
    search_fields = ['id']
    list_filter = ['id', 'project']

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id','idx', 'audio','text']
    list_display_links = ['id']
    search_fields = ['id']
    list_filter = ['id']