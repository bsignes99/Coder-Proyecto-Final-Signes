from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class heroe(models.Model):

    nombre = models.CharField(max_length=40)
    habilidad = models.CharField(max_length=70)
    raza = models.CharField(max_length=40)
    vehiculo = models.CharField(max_length=40)

class villano(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    vehiculo = models.CharField(max_length=100)

class vehiculo(models.Model):
    modelo = models.CharField(max_length= 40)
    propietario = models.CharField(max_length= 40)

class avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #un usuario ya creado
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.usuario}-----{self.imagen}"

class favorito(models.Model):
    nombre = models.CharField(max_length=40)
    habilidad = models.CharField(max_length=70)
    raza = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="Heroes", null=True, blank=True)