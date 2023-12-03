from django.forms import ModelForm
from ..models import Registro


class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'correo_electronico',
            'sexo',
            'destino'
        ]
