from django.urls import path, include

from Arzaizm_istorizm import views

app_name = 'Arxaizm_istorizm'

urlpatterns = [
    path('arxaizm/', views.Arxaizm, name='arzaizm'),
    path('istorizm/', views.Istorizm, name='istorizm'),
    path('arxaizm_save/', views.arxaizm_save, name='arxaizm_save'),
]
