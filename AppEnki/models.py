from django.db import models

class Terapias(models.Model):
    tipo_terapia = models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre de la terapia: {self.tipo_terapia}"
    
class Registro_usuario(models.Model):
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=14)
    correo = models.EmailField()
    def __str__(self):
        return f"Nombre completo: {self.nombre_completo} - Fecha de nacimiento: {self.fecha_nacimiento} - Celular: {self.celular} - Correo: {self.correo}"
    
    
class motivo_terapia(models.Model):
    detalle_usuario = models.CharField(max_length=500)
    def __str__(self):
        return f"Detalles ingresados por el usuario: {self.detalle_usuario}"

    
