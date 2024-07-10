from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'user_auth/login.html')

def user_registration(request):
    pass

def user_logout(request):
    pass