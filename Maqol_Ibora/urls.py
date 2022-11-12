from django.urls import path, include

from Maqol_Ibora import views

app_name = 'maqol_ibora'

urlpatterns = [
    path('maqol/', views.maqol, name='maqol'),
    path('ibora/', views.ibora, name='ibora'),
]
