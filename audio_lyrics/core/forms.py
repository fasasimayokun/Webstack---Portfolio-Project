from django.forms import forms
from .models import MusicPost

class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicPost
        fields = ['artist', 'created_at', 'updated_at']