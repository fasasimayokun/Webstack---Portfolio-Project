from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_registration, name='signup'),
    path('generate-transcript/', views.generate_transcript, name='generate-transcript'),
    path('display-transcripts/', views.display_transcripts, name='display-transcripts'),
    path('transcript-detail/<int:pk>/', views.detail_transcript, name='transcript-detail'),
    path('update-transcript/<int:pk>/', views.update_transcript, name='update-transcript'),
    path('delete-transcript/<int:pk>/', views.delete_transcript, name='delete-transcript'),
]
