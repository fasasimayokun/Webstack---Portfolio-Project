from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import MusicPost
import assemblyai as aai
import openai
import os

from .forms import MusicForm, MusicUpdate
from django.contrib import messages
# Create your views here.

# Handles the index page
@login_required(login_url="login")
def index(request):
    form = MusicForm()
    return render(request, 'index.html', {'form': form})

# processes the file input from the form
@login_required(login_url="login")
def generate_transcript(request):
    # get the data from the post method
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music_path = form.save()
        
            # get the transcription 
    
            transcription = get_transcription(music_path.music_file.path)
            if not transcription:
                messages.success(request, "Music file not successfully transcribed!")
                return JsonResponse({'error': 'something occurred'}, status=500)

            # save blog article to database
            music_post = MusicPost.objects.create(
                user = request.user,
                music_path = music_path,
                generated_lyrics = transcription,
            )
        
            music_post.save()
            # displays a success message
            messages.success(request, "Music file successfully transcribed!")

            # redirects user back to the index page
            return redirect("/")
        else:
            print("something is wrong with the file")

# creates the transcript with assemblyai
def get_transcription(music_path):
    # set the api key for the assemblyai
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

# lists all transcripts
@login_required(login_url="login")
def display_transcripts(request):
    music_post = MusicPost.objects.filter(user=request.user)
    return render(request, 'display.html', {'transcripts': music_post})

# updates a transcript
@login_required(login_url="login")
def update_transcript(request, pk):
    transcript = MusicPost.objects.get(id=pk)

    form = MusicUpdate(instance=transcript)

    if request.method == "POST":
        form = MusicUpdate(request.POST, instance=transcript)

        if form.is_valid():
            form.save()

            messages.success(request, "Your transcript was edited successfully!")

            return redirect(reverse("transcript-detail", args=[transcript.id]))

    context = {"form": form}

    return render(request, "update-transcript.html", context)



# read / view a singular transcript
def detail_transcript(request, pk):
    transcribed_music = MusicPost.objects.get(id=pk)

    context = {"transcript": transcribed_music, 'is_edited': transcribed_music.is_edited}
    return render(request, "transcript-detail.html", context)


# delete a transcript
@login_required(login_url="login")
def delete_transcript(request, pk):
    transcript = MusicPost.objects.get(id=pk)
    transcript.delete()
    messages.success(request, "The transcript was successfully deleted!")
    return redirect("/")


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in!")
            return redirect('/')

    return render(request, 'user_auth/login.html')

# user signup
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
                messages.success(request, "Account created successfully!")
                login(request, user)
                return redirect('login')
            except:
                messages.error(request, "Error creating account")
        else:
            messages.error(request, "Password do not match")

    return render(request, 'user_auth/registration.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout success!")
    return redirect('login')