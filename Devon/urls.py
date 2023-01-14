from django.urls import path, include

from Devon import views

app_name = 'Devon'

urlpatterns = [
    path('devon', views.devon, name='devon'),
    path('in_devon/<int:pk>/', views.in_devon, name='in_devon'),
    path('janrlar', views.janr, name='janr'),
    path('in_janr/<int:pk>/', views.in_janr, name='in_janr'),
    path('janr_misra/<int:pk>/', views.janr_misra, name='janr_misra'),

]
