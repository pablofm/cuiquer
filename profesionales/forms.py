from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField, Select
from profesionales.models import Profesional, Trabajo, Servicio


class ProfesionalForm(ModelForm):
    servicio = ModelChoiceField(
        queryset=Servicio.objects.all(),
        empty_label='* Servicio que ofreces',
        widget=Select(attrs={'class': 'form-control form-alta'}))

    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {
            "servicios": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Servicio que ofreces"}),
            "nombre": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Nombre y apellidos"}),
            "email": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Email"}),
            "telefono": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Teléfono"}),
            "area_servicio": TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Área en la que ofreces el servicio"}),
            "que": Textarea(attrs={'class': 'form-control form-alta', 'rows': 4, 'placeholder': " ¿Qué me apasiona de mi trabajo?"}),
        }


class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'
