from django import forms
from landing.models import Contacto, NewsLetter


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


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
        widgets = {
            "email": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Email"}),
        }
