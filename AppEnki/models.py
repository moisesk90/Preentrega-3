from django.db import models

class Terapias(models.Model):
    tipo_terapia = models.CharField(max_length=50)
    
    
class Registro_usuario(models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=14)
    correo = models.EmailField()
    
class motivo_terapia(models.Model):
    detalle_usuario = models.CharField(max_length=500)

    
