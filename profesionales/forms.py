from django import forms
from profesionales.models import Profesional, Servicio


class ProfesionalForm(forms.ModelForm):
    licencia = forms.BooleanField(initial=False)
    # servicio = forms.ModelChoiceField(
    #     queryset=Servicio.objects.all(),
    #     empty_label='* Servicio que ofreces',
    #     widget=forms.Select(attrs={'class': 'form-control form-alta'})
    # )

    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {
            "servicio": forms.SelectMultiple(attrs={'class': 'form-control form-alta'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Nombre y apellidos"}),
            "email": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Email"}),
            "telefono": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Teléfono"}),
            "area_servicio": forms.TextInput(attrs={'class': 'form-control form-alta', 'placeholder': "* Tu código postal"}),
            "que": forms.Textarea(attrs={'class': 'form-control form-alta', 'rows': 4, 'placeholder': " Algún comentario"}),
        }
