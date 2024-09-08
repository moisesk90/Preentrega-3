
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from. models import Imagen
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView





def login_request(request):
    
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return render(request, "AppEnki/padre.html")
        
        msg_login = "Usuario o contraseña incorrectos"
        
    form = AuthenticationForm()
    return render(request, "AppUsers/login.html", {"form": form, "msg_login": msg_login})
            
        
def register(request):
    
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppEnki/padre.html")
        
        msg_register = "Error en los datos ingresados"
        
    form = UserRegisterForm()
    return render(request, "AppUsers/registro.html", {"form": form, "msg_register": msg_register})
    
@login_required
def editar_perfil(request):
    usuario= request.user
    
    if request.method == 'POST':
        miformulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miformulario.is_valid():
            if miformulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen = miformulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar = Imagen(user=usuario, imagen=miformulario.cleaned_data.get('imagen'))
                    avatar.save()
            miformulario.save()
            
            return render(request, "AppEnki/padre.html")
    
    else:
        miformulario = UserEditForm(instance=usuario)
        
    return render(request, "AppUsers/editar_usuario.html", {"mi_form": miformulario, "usuario": usuario})


class CambiarContrasena(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppUsers/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")