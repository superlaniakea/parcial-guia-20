from django.contrib import admin
from .models import Registro, Reserva, Viaje
# Register your models here.


@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    pass


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    pass


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass
