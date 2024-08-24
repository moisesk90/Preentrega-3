from django.contrib import admin
from AppEnki.models import Terapias, Registro_usuario, motivo_terapia

# Register your models here.

admin.site.register(Terapias)
admin.site.register(Registro_usuario)
admin.site.register(motivo_terapia)