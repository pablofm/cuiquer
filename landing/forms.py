from django import forms
from landing.models import Contacto


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


            
