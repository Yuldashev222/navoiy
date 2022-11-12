from django.urls import path, include

from Gazal import views

app_name = 'Gazal'

urlpatterns = [
    path('gazal', views.gazal, name='gazal'),
    path('in_gazal/<int:pk>/', views.in_gazal, name='in_gazal'),
    path('gazal_meta/<int:pk>/', views.gazal_meta, name='gazal_meta'),
    path('file/', views.file, name='file'),
    path('file_save/', views.file_save, name='file_save'),
    path('file_word/', views.soz_save, name='word_save'),
    path('file_meta/', views.meta_save, name='meta_save'),
]
