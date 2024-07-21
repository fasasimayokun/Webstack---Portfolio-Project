from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class MusicPath(models.Model):
    music_file = models.FileField(upload_to='music/')

    def __str__(self):
        return str(self.music_file)

class MusicPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_path = models.ForeignKey(MusicPath, on_delete=models.CASCADE, default=1)
    generated_lyrics = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_edited(self):
        return self.created_at != self.updated_at
    
    @property
    def transcript_name(self):
        return os.path.basename(self.music_path.music_file.name)

    def __str__(self):
        return f"{self.user.username} - {os.path.basename(self.music_path.music_file.name)}"
    