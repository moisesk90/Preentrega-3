from AppEnki import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario_terapias/', views.terapias_formulario, name='terapias_formulario'),
    path('formulario_usuario/', views.usuarios_formulario, name='usuarios_formulario'),
    path('formulario_motivo/', views.motivo_formulario, name='motivo_formulario'),
    path('buscar/', views.buscar, name='buscar'),
    path('leerterapias/', views.leerterapias, name='leerterapias'),
    path('eliminarterapias/<nombre_terapia>/', views.eliminarterapias, name='eliminarterapias'),
    path('about/', views.about, name='about'),
    
    
]