from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_registration, name='signup'),
    path('generate-lyrics/', views.generate_lyrics, name='generate-lyrics'),
    path('display-lyrics/', views.display_lyrics, name='dispay')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)