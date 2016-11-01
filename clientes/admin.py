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

    def categoria(self, obj):
        return obj.servicio.categoria

    empty_value_display = '???'

    list_display = ('nombre', 'email', 'telefono', 'categoria', 'servicio', 'fecha_solicitud')
    readonly_fields = ('fecha_solicitud', 'detalles_usuario', 'categoria')
    fields = ('fecha_solicitud', 'detalles_usuario', 'categoria', 'servicio', 'codigo_postal', 'observaciones')

admin.site.register(Cliente, ClienteAdmin)
