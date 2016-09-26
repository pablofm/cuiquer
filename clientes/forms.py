from django import forms
from localflavor.es.forms import ESPhoneNumberField
from profesionales.models import Servicio


class ClienteForm(forms.Form):
    licencia = forms.BooleanField(initial=False)
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.all(),
        empty_label='* ¿Qué tipo de servicio necesita?',
        widget=forms.Select(attrs={'class': 'form-control form-alta'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu nombre"}),)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu email"}))
    telefono = ESPhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Un teléfono de contacto"}))
