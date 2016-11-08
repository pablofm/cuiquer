from django import forms
from django.contrib import admin
from clientes.models import Cliente
from clientes.fields import GroupedModelChoiceField
from profesionales.models import Servicio
from perfiles.admin import UsuarioModelAdmin


class ClienteAdminForm(forms.ModelForm):
    servicio = GroupedModelChoiceField(
        queryset=Servicio.objects.all(),
        group_by_field='categoria')

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(UsuarioModelAdmin):
    form = ClienteAdminForm
    servicio = GroupedModelChoiceField(
        queryset=Servicio.objects.all(),
        group_by_field='categoria')

    def categoria(self, obj):
        return obj.servicio.categoria

    list_display = ('nombre', 'email', 'telefono', 'categoria', 'servicio', 'fecha_solicitud')

    readonly_fields = ('fecha_solicitud', 'detalles_usuario', 'categoria', 'origen')

    fieldsets = (
        ('Datos Básicos', {
            'fields': ('fecha_solicitud', 'detalles_usuario', 'origen')
        }),
        ('Datos Generales', {
            'fields': ('categoria', 'servicio', 'codigo_postal'),
        }),
        ('Información extra', {
            'fields': (
                'metodo_trabajo', 'metodo_contacto', 'donde',
                'precio', 'preguntas_especificas', 'informacion_extra', 'observaciones'),
        }),
    )

    class Meta:
        model = Cliente


admin.site.register(Cliente, ClienteAdmin)
