from django.http import HttpResponse
from django.template import Template, Context

def sobrenosotros(request):
    return HttpResponse("Página para alinear los chackras")

def alinchackras(request):
    return HttpResponse("<h1> Que es la aliniación de Chackras? </h1> <p>La aliniación de chackras es una regulación de las energías masculinas y femininas para que tenga una circulación equilibrada. </p>")

def primer_template(request):
    
    html = open('/Users/tenpoadmin/Desktop/Preentrega 3/enki/plantillas/template1.html')
    
    plantilla =  Template(html.read())
    
    html.close()
    
    mi_contexto = Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)