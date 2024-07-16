from django import forms
from .models import MusicPath

class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicPath
        fields = ['music_file',]