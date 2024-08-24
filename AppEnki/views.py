from django.shortcuts import render
from django.http import HttpResponse

def inicio (request):
    return render(request, 'appenki/padre.html')

def terapias(request):
    return render(request, 'appenki/terapias.html')

def usuarios(request):
    return render(request, 'appenki/usuarios.html')

def motivos(request):
    return render(request, 'appenki/motivos.html')


