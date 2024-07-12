from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MusicPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_file = models.FileField(upload_to='music/')
    artist = models.CharField(max_length=100)
    generated_lyrics = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.artist