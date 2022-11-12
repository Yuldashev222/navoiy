from django.urls import path, include

from Devon import views

app_name = 'Devon'

urlpatterns = [
    path('devon', views.devon, name='devon'),
    path('in_devon/<int:pk>/', views.in_devon, name='in_devon'),
]
