
from django.urls import path, include

from Base import views

app_name = 'Base'

urlpatterns = [
    path('', views.index, name='home'),
    path('korpus_haqida/', views.korpus_haqida, name='korpus_haqida'),
    path('maqola/', views.maqola, name='maqola'),
    path('tarjimayi_hol/', views.tarjimayi_hol, name='tarjimayi_hol'),
    path('maqola_pdf/<int:id>/', views.maqola_pdf, name='maqola_pdf'),
    path('mualliflar/', views.mualliflar, name='mualliflar')
]
