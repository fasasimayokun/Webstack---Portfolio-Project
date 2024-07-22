from django import forms
from .models import MusicPath, MusicPost

class MusicForm(forms.ModelForm):
    class Meta:
        model = MusicPath
        fields = ['music_file',]
        widgets = {
            'music_file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border: 2px solid #ccc; padding: 10px; border-radius: 10px;'
            }),
        }


class MusicUpdate(forms.ModelForm):

    class Meta:
        model = MusicPost
        fields = ['generated_lyrics']
        widgets = {
            'generated_lyrics': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 80,
                'rows': 10,
            })
        }
        labels = {
            'generated_lyrics': '',
        }