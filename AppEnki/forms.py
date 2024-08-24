from django import forms


class FormularioTerapias(forms.Form):
    tipo_terapia = forms.CharField(max_length=30)
    
class FormularioUsuarios(forms.Form):
    nombre_completo = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField()
    celular = forms.CharField(max_length=14)
    correo = forms.EmailField()
    
class FormularioMotivo(forms.Form):
    detalle_usuario = forms.CharField(max_length=500)
    