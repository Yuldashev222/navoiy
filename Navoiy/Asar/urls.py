from django.urls import path, include

from Asar import views

app_name = 'Asar'

urlpatterns = [
    path('asar/', views.asar, name='asar'),
]
