from django.urls import path, include

from Sheriy_sanat import views

app_name = 'sheriy_sanat'

urlpatterns = [
    path('talmeh/', views.talmeh, name='talmeh'),
    path('tazod/', views.tazod, name='tazod'),
    path('tanosib/', views.tanosib, name='tanosib'),
    path('tashbeh/', views.tashbeh, name='tashbeh'),
    path('file_talmeh/', views.talmeh_save, name='talmeh_save'),
    path('file_tazod/', views.tazod_save, name='tazod_save'),
    path('file_tanosib/', views.tanosib_save, name='tanosib_save'),
    path('file_tashbih/', views.tashbih_save, name='tashbih_save'),
]
