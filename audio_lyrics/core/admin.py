from django.contrib import admin
from .models import MusicPath, MusicPost

# Register your models here.
admin.site.register(MusicPath)
admin.site.register(MusicPost)