from django.http import HttpResponse

def sobrenosotros(request):
    return HttpResponse("Página para alinear los chackras")

def alinchackras(request):
    return HttpResponse("<h1> Que es la aliniación de Chackras? </h1> <p>La aliniación de chackras es una regulación de las energías masculinas y femininas para que tenga una circulación equilibrada. </p>")