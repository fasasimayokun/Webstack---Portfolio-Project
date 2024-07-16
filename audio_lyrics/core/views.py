from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import MusicPost
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import assemblyai as aai
import json
import openai
import os
import time

from .forms import MusicForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
# Create your views here.

def index(request):
    form = MusicForm()
    return render(request, 'index.html', {'form': form})

def generate_lyrics(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music_path = form.save()
        
        # get the 
    
            transcription = get_transcription(music_path.music_file.path)
            if not transcription:
                print("no transcription")
                return# return JsonResponse({'error': "Failed to get transcript"}, status=500)

            # # use openAI to generate the blog
            # music_content = generate_blog_from_transcription(transcription)
            # print(music_content)
            #     return# return JsonResponse({'error': "Failed to generate blog article"}, status=500)

            # save blog article to database
            music_post = MusicPost.objects.create(
                user = request.user,
                music_path = music_path,
                generated_lyrics = transcription,
            )
        
            music_post.save()
            
            if music_post.generated_lyrics:
                generated_lyrics = music_post.generated_lyrics
                return render(request, 'display.html', {'content': generated_lyrics})
            
            # return blog article as a response
            return render(request, 'index.html', {'content': get_transcription})
        else:
            print("something is wrong with the file")
    # else:
    #     form = MusicForm()
    # return render(request, 'index.html', {'form': form})
        

def get_transcription(music_path):
    aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')

    transcriber = aai.Transcriber()

    audio_url = music_path

    config = aai.TranscriptionConfig(speaker_labels=True)

    transcript = transcriber.transcribe(audio_url, config)
    if transcript.status == aai.TranscriptStatus.error:
        print(transcript.error)
    
    return transcript.text

# def generate_blog_from_transcription(transcription):
#     openai.api_key = os.getenv('ASSEMBLYAI_KEY')

#     prompt = f"Based on the following transcript from a music file, write a comprehensive understanding and insight of the music lyrics, write it based on the transcript, but dont make it easy to understand:\n\n{transcription}\n\nMusic Lyrics:"

    
#     try:
#         response = openai.Completion.create(
#             model="text-embedding-3-large	",
#             prompt=prompt,
#             max_tokens=150
#         )
#         generated_content = response.choices[0].text.strip()
#         return generated_content
#     except openai.error.RateLimitError:
#         print("Rate limit exceeded. Retrying in 10 seconds...")
#     except openai.error.OpenAIError as e:
#         print(f"An error occurred: {e}")



def display_lyrics(request):
    
    music_post = MusicPost.objects.all()
    return render(request, 'display.html', {'contents': music_post})

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'user_auth/login.html')

def user_registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username,email,password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                pass
        else:
            pass

    return render(request, 'user_auth/registration.html')

def user_logout(request):
    logout(request)