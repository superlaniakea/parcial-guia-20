from django.shortcuts import render
from django.shortcuts import render, redirect
from .formulario.RegistroForm import RegistroForm
from .formulario.ReservaForm import ReservaForm
from .formulario.ViajeForm import ViajeForm
from .formulario.LoginForm import LoginForm
from .formulario.Re_userForm import NewUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registro, Reserva, Viaje
from django.contrib import messages


def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
    return render(request, "Reg_user.html", {"form": formulario})


def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = LoginForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Cambio realizado aquí
            else:
                messages.error(
                    request, "Usuario o contraseña incorrectos. Intente de nuevo.")
    else:
        formulario = LoginForm()
    return render(request, 'login.html', {'form': formulario})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')  # Cambio realizado aquí


def index(request):
    registros = Registro.objects.all()
    reserva = Reserva.objects.all()
    viajes = Viaje.objects.all()
    return render(request, 'index.html', {'registros': registros, 'reserva': reserva, 'viajes': viajes})


def agregar_registro(request):
    if request.method == "POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            registro = formulario.save()  # Guarda el formulario y obtén el objeto de registro
            return redirect('registro', id=registro.id)
    else:
        formulario = RegistroForm()
    return render(request, "agregar_registro.html", {"form": formulario})


def registro(request):
    registros = Registro.objects.all()
    return render(request, 'registro.html', {'registros': registros})


def reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva.html', {'reservas': reservas})


def agregar_reserva(request):
    if request.method == "POST":
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = ReservaForm()
    return render(request, "agregar_reserva.html", {"form": formulario})


def eliminar_registro(request, id):
    Registro.objects.get(id=id).delete()
    return HttpResponseRedirect(request.path_info)


def eliminar_reserva(request, id):
    Reserva.objects.get(id=id).delete()
    return HttpResponseRedirect(request.path_info)


def crear_viaje(request):
    if request.method == "POST":
        formulario = ViajeForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Redirige a la vista deseada después de guardar el viaje
            return HttpResponseRedirect("/")
    else:
        formulario = ViajeForm()

    return render(request, 'crear_viaje.html', {'form': formulario})


def viaje(request):
    viajes = Viaje.objects.all()
    return render(request, 'viaje.html', {'viajes': viajes})


@login_required(login_url='login')
def mi_vista_restringida(request):
    # Lógica de la vista restringida
    return render(request, 'mi_vista_restringida.html')


def blog(request):
    # Lógica de la vista del blog aquí
    return render(request, 'blog.html')


def inicio(request):
    # Tu lógica de vista aquí
    return render(request, 'index.html')
