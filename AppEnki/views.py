from django.shortcuts import render
from django.http import HttpResponse
from AppEnki.models import Terapias, Registro_usuario, motivo_terapia
from AppEnki.forms import FormularioTerapias, FormularioUsuarios, FormularioMotivo
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from AppUsers.views import UserEditForm, UserRegisterForm


def inicio (request):
    return render(request, 'appenki/padre.html')

@login_required
def terapias(request):
    return render(request, 'appenki/terapias.html')

@login_required
def usuarios(request):
    return render(request, 'appenki/usuarios.html')

@login_required
def motivos(request):
    return render(request, 'appenki/motivos.html')

@login_required
def terapias_formulario(request):
    if request.method == 'POST':
        miformulario = FormularioTerapias(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            terapia = Terapias(tipo_terapia=informacion["tipo_terapia"])
            terapia.save()
            return render(request, "AppEnki/padre.html")
    else:
        miformulario = FormularioTerapias()
        
    return render(request, "AppEnki/terapias_formulario.html", {"miformulario": miformulario})

@login_required
def usuarios_formulario(request):
    if request.method == 'POST':
        miformulario = FormularioUsuarios(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            datos = Registro_usuario(nombre_completo=informacion["nombre_completo"], fecha_nacimiento=informacion["fecha_nacimiento"], celular=informacion["celular"], correo=informacion["correo"])
            datos.save()
            return render(request, "AppEnki/padre.html")
    else:
        miformulario = FormularioUsuarios()
        
    return render(request, "AppEnki/usuario_formulario.html", {"miformulario": miformulario})

@login_required
def motivo_formulario(request):
    if request.method == 'POST':
        miformulario = FormularioMotivo(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            motiv = motivo_terapia(detalle_usuario=informacion["detalle_usuario"])
            motiv.save()
            return render(request, "AppEnki/padre.html")
    else:
        miformulario = FormularioMotivo()
        
    return render(request, "AppEnki/motivo_formulario.html", {"miformulario": miformulario})


@login_required
def buscar(request):
    if request.method == 'POST':
        busqueda = request.POST['buscar']
        resultados_terapias = Terapias.objects.filter(tipo_terapia__icontains=busqueda)
        resultados_usuarios = Registro_usuario.objects.filter(nombre_completo__icontains=busqueda) | Registro_usuario.objects.filter(fecha_nacimiento__icontains=busqueda) | Registro_usuario.objects.filter(celular__icontains=busqueda) | Registro_usuario.objects.filter(correo__icontains=busqueda)
        resultados_motivos = motivo_terapia.objects.filter(detalle_usuario__icontains=busqueda)
        return render(request, "AppEnki/buscar.html", {'resultados_terapias': resultados_terapias, 'resultados_usuarios': resultados_usuarios, 'resultados_motivos': resultados_motivos})
    else:
        return render(request, "AppEnki/buscar.html")

@login_required
def leerterapias(request):
    terapia = Terapias.objects.all()
    contexto = {"terapia":terapia}
    return render(request, "AppEnki/leerterapias.html", contexto)

@login_required
def eliminarterapias(request, nombre_terapia):
    terapia = Terapias.objects.get(tipo_terapia=nombre_terapia)
    terapia.delete()
    
    terapias = Terapias.objects.all()
    contexto = {"terapias": terapias}
    return render(request, "Appenki/leerterapias.html", contexto)

def about(request):
    return render(request, 'AppEnki/about.html')


        
    