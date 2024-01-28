from django.shortcuts import render, redirect
import random
from pawPatrol.models import *
from pawPatrol.forms import *
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

def villanos(request):
    return render(request, "villanos.html")

def vehiculos(request):
    return render(request, "vehiculos.html")

def comencemos(request):
    return render(request, "comencemos.html")

def padre(request):
    return render(request, "padre.html")

def heroes(request):
    return render(request, "heroes.html")
@login_required
def tufavorito(request):
    return render(request, "favorito.html")

@login_required
def agregarFavorito(request):
    if request.method == "POST":
        formfav = formularioFavorito(request.POST) #obtiene los datos
        if formfav.is_valid():
            info = formfav.cleaned_data #para tenerlo en modo diccionario
            formfav = favorito( nombre=info["nombre"], habilidad= info["habilidad"], raza=info["raza"],
                                descripcion = info["descripcion"])
            formfav.save()
            return redirect("favorito")
    else:
        formfav = formularioFavorito()

    return render(request, "formfav.html", {"nuevofav":formfav})

@login_required
def verheroe(request):      
    favoritos = favorito.objects.all()
    contexto = {"favoritos": favoritos}
    return render(request, "verheroe.html", contexto)

@login_required
def actualizarfav(request, nombreHeroe):

        upheroe = favorito.objects.get(nombre = nombreHeroe)
        
        if request.method == "POST":
            formu= formularioFavorito(request.POST)
            if formu.is_valid():
                info = formu.cleaned_data
                upheroe.nombre= info["nombre"]
                upheroe.raza= info["raza"]
                upheroe.habilidad= info["habilidad"]
                upheroe.descripcion= info["descripcion"]

                upheroe.save()

                return redirect("favorito")

        else:
            formu = formularioFavorito(initial={"nombre":upheroe.nombre, "raza":upheroe.raza,
                                                "habilidad": upheroe.habilidad, "descripcion": upheroe.descripcion})

        return render(request, "editarheroe.html", {"formu":formu, "nombre":nombreHeroe})        

@login_required
def eliminarfav(request, nombreHeroe):  
        delheroe = favorito.objects.get(nombre = nombreHeroe)
        delheroe.delete()

        heroes = favorito.objects.all()

        return redirect("favorito")

@login_required
def agregarHeroe(request):
    
    if request.method == "POST":
        nuevo_form = formularioHeroes(request.POST) #obtiene los datos
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data #para tenerlo en modo diccionario
            nuevoHeroe = heroe(nombre=info["nombre"], raza=info["raza"], 
                               habilidad=info["habilidad"], vehiculo=info["vehiculo"])
            nuevoHeroe.save()
            return redirect("heroes")
    else:
        nuevo_form = formularioHeroes()

    return render(request, "formheroe.html", {"nuevoheroe":nuevo_form})


@login_required
def agregarVillano(request):
    if request.method == "POST":
        formVillano = formularioVillano(request.POST) #obtiene los datos
        if formVillano.is_valid():
            info = formVillano.cleaned_data #para tenerlo en modo diccionario
            formVillano = villano(nombre=info["nombre"],raza=info["raza"], vehiculo = info["vehiculo"])
            formVillano.save()
            return redirect("villanos")

    else:
        formVillano = formularioVillano()

    return render(request, "formvillano.html", {"nuevovillano":formVillano})

@login_required
def agregarVehiculo(request):
    
    if request.method == "POST":
        formVehiculo = formularioVehiculo(request.POST) #obtiene los datos
        if formVehiculo.is_valid():
            info = formVehiculo.cleaned_data #para tenerlo en modo diccionario
            nuevoVehiculo = vehiculo(modelo=info["modelo"],propietario=info["propietario"])
            nuevoVehiculo.save()
            return redirect("vehiculos")
    else:
        formVehiculo = formularioVehiculo()

    return render(request, "formvehiculo.html", {"nuevovehiculo":formVehiculo})


def heroesdos(request):

    return render(request, "heroessig.html")

def vehiculodos(request):

    return render(request, "vehiculossig.html")


def buscarheroe(request):
    return render(request, "buscarheroe.html")

def resultados(request):
    if request.method == "GET":

        pedido = request.GET["nombre"]
        resultado = heroe.objects.filter(nombre__icontains=pedido)

        return render(request, "resultados.html", {"nombre":resultado})
    else:
        respuesta= "No existen datos"
        return HttpResponse(respuesta)
 

def log(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            
            info = form.cleaned_data

            usuario = info["username"]
            contraseña = info["password"]    

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)

                return redirect("inicio")
            else:
                return render(request, "inicio.html", {"msj":f"Datos incorrectos"})

        else:
            return render(request, "inicio.html", {"msj":f"Formuario erroneo"})


    formulario= AuthenticationForm()
    
    return render(request, "registro/login.html", {"form":formulario})

def registrar(request):
    
    if request.method == "POST":
        form= registro(request.POST)

        if form.is_valid():
            
            info = form.cleaned_data

            usuario= info["username"]

            form.save()

            return redirect("inicio")
    else:
        form = registro()

    return render(request, "registro/registrar.html", {"form":form}) 

def cerrar_sesion(request):

    logout(request)

    return render(request, "registro/logout.html", {"msj": f"Has cerrado sesión"}) 

@login_required
def editar_perfil(request):
    usuario =  request.user
    if request.method == "POST":
        if request.method == "POST":
            form = editar(request.POST)

            if form.is_valid():
                
                info = form.cleaned_data
    
                usuario.first_name= info["first_name"]
                usuario.last_name= info["larst_name"]
                usuario.email= info["email"]
                usuario.set_password= info["password1"]

                usuario.save()
                return render(request, "inicio.html")
    else:
         form= editar(initial={"first_name": usuario.first_name,
                               "last_name": usuario.last_name,
                               "email": usuario.email})

    return render(request, "registro/editarUsuario.html", {"form":form})

@login_required
def editar_avatar(request):
    if request.method == "POST":
        formu = editarAvatar(request.POST, request.FILES)

        if formu.is_valid():

            info = formu.cleaned_data

            imagen = avatar(usuario= request.user , imagen= info["imagen"])

            imagen.save()

            return redirect("inicio")
    else:
        formu = editarAvatar()

    return render(request, "registro/editarAvatar.html", {"formu": formu})

def sobremi(request):

    return render(request, "aboutme.html")
