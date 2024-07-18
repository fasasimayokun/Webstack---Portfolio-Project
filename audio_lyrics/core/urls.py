from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_registration, name='signup'),
    path('generate-transcript/', views.generate_transcript, name='generate-lyrics'),
    path('display-transcripts/', views.display_transcripts, name='dispay'),
    path('transcript-detail/<int:pk>/', views.singular_transcript, name='transcript-detail'),
    path("update-transcript/<int:pk>/", views.update_transcript, name="update-transcript"),
    path("delete-transcript/<int:pk>/", views.delete_transcript, name="delete-transcript"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)