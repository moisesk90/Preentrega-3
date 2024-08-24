from django.shortcuts import render
from django.http import HttpResponse
from AppEnki.models import Terapias, Registro_usuario, motivo_terapia
from AppEnki.forms import FormularioTerapias, FormularioUsuarios, FormularioMotivo

def inicio (request):
    return render(request, 'appenki/padre.html')

def terapias(request):
    return render(request, 'appenki/terapias.html')

def usuarios(request):
    return render(request, 'appenki/usuarios.html')

def motivos(request):
    return render(request, 'appenki/motivos.html')

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

    


