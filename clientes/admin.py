from django.contrib import admin
from clientes.models import Cliente
from clientes.fields import GroupedModelChoiceField
from profesionales.models import Servicio
from perfiles.admin import UsuarioModelAdmin


class ClienteAdmin(UsuarioModelAdmin):
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
            'fields': ('metodo_trabajo', 'metodo_contacto', 'donde', 'precio', 'informacion_extra', 'observaciones'),
        }),
    )

    class Meta:
        model = Cliente

admin.site.register(Cliente, ClienteAdmin)
