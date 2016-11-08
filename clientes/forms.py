from django import forms
from localflavor.es.forms import ESPhoneNumberField
from profesionales.models import Servicio, ORIGEN_CHOICES
from perfiles.models import Usuario
from clientes.models import Cliente
from clientes.fields import GroupedModelChoiceField


class ClienteForm(forms.Form):
    licencia = forms.BooleanField(initial=False)
    servicio = GroupedModelChoiceField(
        queryset=Servicio.objects.all(),
        empty_label='* ¿Qué tipo de servicio necesita?',
        group_by_field='categoria',
        widget=forms.Select(attrs={'class': 'form-control form-alta'}))

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu nombre"}),)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu email"}))
    telefono = ESPhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Un teléfono de contacto"}))

    ORIGEN_CHOICES = (('', '* ¿Cómo nos has conocido?'),) + ORIGEN_CHOICES

    origen = forms.ChoiceField(
        choices=ORIGEN_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form-alta'}))

    def is_valid(self):
        valid = super(ClienteForm, self).is_valid()
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
        servicio = self.cleaned_data["servicio"]
        origen = self.cleaned_data["origen"]

        usuario = Usuario.objects.create(email=email, nombre=nombre, telefono=telefono)
        usuario.set_password(email)
        usuario.save()

        cliente = Cliente.objects.create(servicio=servicio, usuario=usuario, origen=origen)
        return cliente
