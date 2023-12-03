"""
URL configuration for parcial20 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dubai import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('agregar_registro/', views.agregar_registro, name='agregar_registro'),
    path('agregar_reserva/', views.agregar_reserva, name='agregar_reserva'),
    path('eliminar_registro/<int:id>/',
         views.eliminar_registro, name='eliminar_registro'),
    path('eliminar_reserva/<int:id>/',
         views.eliminar_reserva, name='eliminar_reserva'),
    # Ruta URL para la vista 'login'
    path('login/', views.iniciar_sesion, name='login'),
    # Ruta URL para la vista 'reg_user'
    path('reg_user/', views.reg_user, name='reg_user'),
    path('registro/', views.registro, name='registro'),
    path('blog/', views.blog, name='blog'),
    path('reserva/', views.reserva, name='reserva'),
    path('crear_viaje/', views.crear_viaje, name='crear_viaje'),
    path('viaje/', views.viaje, name='viaje'),
]
