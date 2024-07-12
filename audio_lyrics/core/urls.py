from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_registration, name='signup'),
    path('generate-lyrics/', views.generate_lyrics, name='generate-lyrics'),
]