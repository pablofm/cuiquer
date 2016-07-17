from django.forms import ModelForm, TextInput, Textarea
from profesionales.models import Profesional, Trabajo


# Create the form class.
class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {
            "servicio": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Servicio que ofreces"}),
            "nombre": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Nombre"}),
            "dni": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* DNI"}),
            "fecha_nacimiento": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Fecha de Nacimiento"}),
            "email": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Correo electrónico"}),
            "telefono": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Teléfono"}),
            "lugar_de_residencia": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Lugar de residencia"}),
            "radio_prestacion": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "* Radio(en Km) de prestación del servicio"}),
            "web": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "Enlace a su página web"}),
            "linkedin": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "LinkedIn"}),
            "nombre_empresa": TextInput(attrs={'class': 'form-control form-alta-profesional', 'placeholder': "Nombre de la empresa"}),
            "como": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 4, 'placeholder': "* ¿Cómo trabajo? ¿Cómo presto el servicio?"}),
            "que": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 4, 'placeholder': "* ¿Qué me apasiona de mi trabajo?"}),
            "experiencia": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 4, 'placeholder': "* ¿Cuanto tiempo llevo ofreciendo este tipo de servicio?"}),
            "consejo": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 4, 'placeholder': "¿Qué consejo das a un cliente que busque contratar este tipo de servicio?"}),
            "formacion": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 4, 'placeholder': "¿Qué formación o experiencia relevante tienes relacionada con el servicio que ofreces?"}),
            "tipo_cliente": Textarea(attrs={'class': 'form-control form-alta-profesional', 'rows': 3, 'placeholder': "¿Con qué tipo de clientes te gustaría trabajar?"}),
        }


class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'
