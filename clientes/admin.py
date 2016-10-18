from django.contrib import admin
from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = (
        'usuario__nombre', 'usuario__email', 'usuario__telefono', 'fecha_solicitud', 'categoria', 'servicio')
    list_display = (
        'usuario__nombre', 'usuario__email', 'usuario__telefono', 'servicio', 'fecha_solicitud', 'observaciones')
    exclude = ('usuario',)

    def usuario__nombre(self, obj):
        return obj.usuario.nombre

    def usuario__email(self, obj):
        return obj.usuario.email

    def usuario__telefono(self, obj):
        return obj.usuario.telefono

    def categoria(self, obj):
        return obj.servicio.categoria

    usuario__nombre.short_description = "Nombre"
    usuario__email.short_description = "Email"
    usuario__telefono.short_description = "Teléfono"

admin.site.register(Cliente, ClienteAdmin)
