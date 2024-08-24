from AppEnki import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('terapias/', views.terapias, name='terapias'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('motivo/', views.motivos, name='motivos'),
    path('formulario_terapias/', views.terapias_formulario, name='terapias_formulario'),

]