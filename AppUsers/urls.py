from django.urls import path
from AppUsers import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('registro/', views.register, name="registro"),
    path('logout/', LogoutView.as_view(template_name='AppEnki/padre.html'), name="logout"),
    path('editar/', views.editar_perfil, name="editar_perfil"),
    path('cambiar_pass', views.CambiarContrasena.as_view(), name="cambiar_pass"), 
    
    
    
]