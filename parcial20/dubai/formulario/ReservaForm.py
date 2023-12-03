from django.forms import ModelForm
from ..models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'correo_electronico',
            'sexo',
            'destino',
            'fecha_inicio',
            'fecha_fin',
            'cantidad_adultos',
            'cantidad_menores',
        ]
