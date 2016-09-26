from django import forms
from landing.models import Contacto, Suscripcion


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Nombre"}),
            "email": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Email"}),
            "asunto": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Asunto"}),
            "mensaje": forms.Textarea(attrs={'class': 'form-control form-alta', 'rows': 4, 'placeholder': "* Mensaje"}),
        }


class SuscripcionForm(forms.ModelForm):
    def is_valid(self):
        valid = super(SuscripcionForm, self).is_valid()
        if not valid:
            return False
        emails = [m.email for m in Suscripcion.objects.all()]
        if self.data["email"] in emails:
            return False

        return True

    class Meta:
        model = Suscripcion
        fields = ['email']
        widgets = {
            "email": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Introduce tu email"}),
        }
