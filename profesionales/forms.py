from django.forms import ModelForm, TextInput
from profesionales.models import Profesional, Trabajo


# Create the form class.
class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {
            "servicio": TextInput(attrs={'class': 'form-control'}),
        }


class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'
