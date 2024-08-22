from AppEnki import views
from django.urls import path

urlpatterns = [
    path('inicio/', views.inicio),
    path('terapias/', views.terapias),
    path('usuarios/', views.usuarios),
    path('motivo/', views.motivos),
   

]