from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import MusicPost
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import assemblyai as aai
import json
import openai
import os
# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def generate_lyrics(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            music_file = data['file']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)
        
        
        # get the transcript
        transcription = get_transcription(music_file)
        if not transcription:
            return JsonResponse({'error': "Failed to get transcript"}, status=500)

        # use openAI to generate the blog
        music_content = generate_blog_from_transcription(transcription)
        if not music_content:
            return JsonResponse({'error': "Failed to generate blog article"}, status=500)

        # save blog article to database
        music_lyrics = MusicPost.objects.create(user=request.user, music_file=music_file, artist='', generated_lyrics='')
        music_lyrics.save(commit=False)
        audio = MP3(music_lyrics.music_file.path, ID3=EasyID3)
        music_artist = audio.get('artist', [None])[0] or music_lyrics.artist

        music_lyrics = MusicPost.objects.create(user=request.user,
                                         music_file=music_file,
                                         artist=music_artist,
                                         generated_lyrics=music_content)
        music_lyrics.save()

        # return blog article as a response
        return JsonResponse({'content': music_content})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
        
        
def get_transcription(music_file):
    audio_file = music_file
    aai.settings.api_key = os.getenv('ASSEMBLYAI_KEY')

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    print(transcript.text)
    return transcript.text

def generate_blog_from_transcription(transcription):
    openai.api_key = os.getenv("OPENAI_KEY")

    prompt = f"Based on the following transcript from a music file, write a comprehensive understanding and insight of the music lyrics, write it based on the transcript, but dont make it easy to understand:\n\n{transcription}\n\nMusic Lyrics:"

    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        prompt = prompt,
        max_tokens = 1000
    )

    generated_content = response.choices[0].text.strip()

    return generated_content

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