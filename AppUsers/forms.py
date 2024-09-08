from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from AppEnki.models import Registro_usuario

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email"]
        help_text = {k: "" for k in fields}
        
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name= forms.CharField(label="Apellido", required=False)
    imagen= forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'imagen']
        help_text = {k:"" for k in fields}
        
    