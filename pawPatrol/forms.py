from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pawPatrol.models import *

class formularioHeroes(forms.Form):
    nombre = forms.CharField(max_length=40)
    habilidad = forms.CharField(max_length=70)
    raza = forms.CharField(max_length=40)
    vehiculo = forms.CharField(max_length=40)

class formularioVillano(forms.Form):
    nombre = forms.CharField()
    raza = forms.CharField()
    vehiculo = forms.CharField()

class formularioVehiculo(forms.Form):
    modelo= forms.CharField(max_length= 40)
    propietario = forms.CharField(max_length= 40)

class formularioFavorito(forms.Form):
    nombre = forms.CharField(max_length=40)
    habilidad = forms.CharField(max_length=70)
    raza = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=300)
            

class registro(UserCreationForm):
    username = forms.CharField(label="Ingrese su username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Ingrese la contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese su nombre")
    last_name = forms.CharField(label="Ingrese su apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class editar(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Ingrese la contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese su nombre")
    last_name = forms.CharField(label="Ingrese su apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]

class editarAvatar(forms.ModelForm):

    class Meta:
        model = avatar
        fields = ["imagen"]
