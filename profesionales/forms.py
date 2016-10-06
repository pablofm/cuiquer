from django import forms
from localflavor.es.forms import ESPhoneNumberField
from profesionales.models import Servicio
from profesionales.models import Profesional
from perfiles.models import Usuario


class ProfesionalForm(forms.Form):
    licencia = forms.BooleanField(initial=False)
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple())
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu Nombre"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu email"}))
    telefono = ESPhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Un teléfono de contacto"}))
    codigo_postal = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu código postal"}))

    def servicios_seleccionados(self):
        return self.cleaned_data["servicios"]

    def is_valid(self):
        valid = super(ProfesionalForm, self).is_valid()
        print(self.data)
        if not valid:
            return False
        if Usuario.objects.filter(email=self.data["email"]).exists():
            self.add_error('email', 'Este email ya está registrado')
            return False
        return True

    def save(self):
        nombre = self.cleaned_data["nombre"]
        email = self.cleaned_data["email"]
        telefono = self.cleaned_data["telefono"]
        codigo_postal = self.cleaned_data["codigo_postal"]
        servicios = self.cleaned_data["servicios"]

        usuario = Usuario.objects.create(email=email, nombre=nombre, telefono=telefono)
        usuario.set_password(email)
        usuario.save()

        profesional = Profesional.objects.create(codigo_postal=codigo_postal, usuario=usuario)
        profesional.servicios = servicios

        return profesional
