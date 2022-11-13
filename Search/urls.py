from django.urls import path

from Search import views

app_name = 'Search'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search_result/', views.search_result, name='search_result'),
    path('search_special/', views.search_special, name='search_special'),
]
