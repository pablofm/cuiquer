from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from clientes.models import Cliente
from profesionales.models import Servicio
from localflavor.es.forms import ESPhoneNumberField


class ClienteForm(ModelForm):
    servicio = ModelChoiceField(
        queryset=Servicio.objects.all(),
        empty_label='* ¿Qué tipo de servicio necesita?',
        widget=Select(attrs={'class': 'form-control form-alta'}))
    telefono = ESPhoneNumberField(
        widget=TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Un teléfono de contacto"}))

    class Meta:
        model = Cliente
        fields = ['servicio', 'nombre_cliente', 'telefono', 'email']
        widgets = {
            "nombre_cliente": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "Tu nombre"}),
            "email": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu email"}),
        }
