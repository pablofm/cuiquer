from django import forms
from localflavor.es.forms import ESPhoneNumberField
from profesionales.models import Servicio
from profesionales.models import Profesional, METODO_TRABAJO_CHOICES
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

    ORIGEN_CHOICES = (
        ('', '* ¿Cómo nos has conocido?'),
        (1, 'Amigo'),
        (2, 'Email'),
        (3, 'Buscador'),
        (4, 'Facebook'),
        (5, 'Twitter'),
        (6, 'Instagram'),
        (7, 'Milanuncios'),
        (8, 'JobToday'),
        (9, 'otros')
    )

    origen = forms.ChoiceField(
        choices=ORIGEN_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control form-alta'}))

    def servicios_seleccionados(self):
        try:
            return self.cleaned_data["servicios"]
        except:
            return None

    def is_valid(self):
        valid = super(ProfesionalForm, self).is_valid()
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
        origen = self.cleaned_data["origen"]
        origen_verbose = self.ORIGEN_CHOICES[int(origen)][1]

        usuario = Usuario.objects.create(email=email, nombre=nombre, telefono=telefono)
        usuario.set_password(email)
        usuario.save()

        profesional = Profesional.objects.create(
            usuario=usuario,
            codigo_postal=codigo_postal,
            origen=origen_verbose)
        profesional.servicios = servicios
        profesional.save()
        return profesional


class ProfesionalExtraForm(forms.Form):
    profesional = None
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu Nombre"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu email"}))
    telefono = ESPhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Un teléfono de contacto"}))
    codigo_postal = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu código postal"}))
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple())

    METODO_CHOICES = (('', '* ¿Cómo trabajas?'),) + METODO_TRABAJO_CHOICES
    metodo_trabajo = forms.ChoiceField(
        choices=METODO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control form-alta'}))

    fecha_nacimiento = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Fecha de nacimiento"}))
    foto = forms.ImageField()
    precio = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Precio/hora estimado"}))

    facebook = forms.URLField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control form-alta', 'placeholder': "Enlace página web o Facebook"}))
    linkedin = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "Enlace perfil de linkedin"}))

    formacion_relacionada = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control form-alta', 'placeholder': "¿Qué formación tienes?"}))
    opiniones_clientes = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control form-alta', 'placeholder': "¿Qué dicen tus clientes de ti?"}))

    def __init__(self, *args, **kwargs):
        self.profesional = kwargs.pop('profesional')
        if not self.profesional:
            raise KeyError
        super().__init__(*args, **kwargs)
        self.initial['nombre'] = self.profesional.usuario.nombre
        self.initial['email'] = self.profesional.usuario.email
        self.initial['telefono'] = self.profesional.usuario.telefono
        self.initial['codigo_postal'] = self.profesional.codigo_postal
        self.initial['servicios'] = self.profesional.servicios.all()

    def servicios_seleccionados(self):
        try:
            return self.cleaned_data["servicios"]
        except:
            return self.profesional.servicios.all()

    def is_valid(self):
        valid = super(ProfesionalExtraForm, self).is_valid()
        if not valid:
            print(self.errors)
            return False
        return True

    def save(self):
        profesional = Profesional.objects.get(id=self.profesional.id)
        print(profesional)

        nombre = self.cleaned_data["nombre"]
        email = self.cleaned_data["email"]
        telefono = self.cleaned_data["telefono"]
        foto = self.cleaned_data["foto"]
        codigo_postal = self.cleaned_data["codigo_postal"]
        servicios = self.cleaned_data["servicios"]
        metodo_trabajo = self.cleaned_data["metodo_trabajo"]
        fecha_nacimiento = self.cleaned_data["fecha_nacimiento"]
        precio = self.cleaned_data["precio"]
        facebook = self.cleaned_data["facebook"]
        linkedin = self.cleaned_data["linkedin"]
        formacion_relacionada = self.cleaned_data["formacion_relacionada"]
        opiniones_clientes = self.cleaned_data["opiniones_clientes"]

        usuario = profesional.usuario

        usuario.nombre = nombre
        usuario.email = email
        usuario.telefono = telefono
        usuario.foto = foto
        usuario.save()
        profesional.codigo_postal = codigo_postal
        profesional.servicios = servicios
        profesional.metodo_trabajo = metodo_trabajo
        profesional.fecha_nacimiento = fecha_nacimiento
        profesional.precio = precio
        profesional.facebook = facebook
        profesional.linkedin = linkedin
        profesional.formacion_relacionada = formacion_relacionada
        profesional.opiniones_clientes = opiniones_clientes
        profesional.save()
        return profesional
