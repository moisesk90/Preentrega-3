from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from AppEnki.models import Terapias, Registro_usuario, motivo_terapia

def sobrenosotros(request):
    return HttpResponse("Página para alinear los chackras")

def alinchackras(request):
    return HttpResponse("<h1> Que es la aliniación de Chackras? </h1> <p>La aliniación de chackras es una regulación de las energías masculinas y femininas para que tenga una circulación equilibrada. </p>")

def primer_template(request):
    
    nom = "moises"
    ap = "irarrazabal"
    diccionario = {"nombre": nom, "apellido": ap}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregar_terapia(request, terap):
    terapia = Terapias(tipo_terapia=terap)
    terapia.save()
    
    return HttpResponse("Terapia agregada con éxito!!")

def agregar_usuario(request, nom, fech_nac, cel, corr):
    datos = Registro_usuario(nombre_completo=nom, fecha_nacimiento=fech_nac, celular=cel, correo=corr)
    datos.save()
    return HttpResponse("Tus datos han sido guardado exitosamente!!")

def agregar_motivo(request, motiv):
    texto = motivo_terapia(detalle_usuario=motiv)
    texto.save()
    return HttpResponse("Hola!! Tu mensaje ha sido guardado con éxito!!!")
    