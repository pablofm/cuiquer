from django.forms import ModelForm, TextInput, Textarea
from profesionales.models import Profesional, Trabajo
from localflavor.es.forms import ESIdentityCardNumberField


class ProfesionalForm(ModelForm):
    dni = ESIdentityCardNumberField(widget=TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* DNI"}))

    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {
            "servicio": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Servicio que ofreces"}),
            "nombre": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Nombre"}),
            "email": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Correo electrónico"}),
            "telefono": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Teléfono"}),
            "lugar_de_residencia": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Lugar de residencia"}),
            "que": Textarea(attrs={'class': 'form-control form-alta', 'rows': 4, 'placeholder': "* ¿Qué me apasiona de mi trabajo?"}),
        }


class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'
