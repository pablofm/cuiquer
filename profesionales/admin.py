from django.contrib import admin
from profesionales.models import Profesional, Servicio, Categoria


class ProfesionalAdmin(admin.ModelAdmin):
    fields = ('usuario__nombre', 'usuario__email', 'usuario__telefono', 'codigo_postal', 'servicios')
    readonly_fields = ('usuario__nombre', 'usuario__email', 'usuario__telefono')
    list_display = (
        'usuario__nombre', 'usuario__email', 'usuario__telefono', 'codigo_postal', 'fecha_ultima_modificacion')
    list_filter = ['servicios']
    exclude = ('usuario',)

    def usuario__nombre(self, obj):
        return obj.usuario.nombre

    def usuario__email(self, obj):
        return obj.usuario.email

    def usuario__telefono(self, obj):
        return obj.usuario.telefono
    usuario__nombre.short_description = "Nombre"
    usuario__email.short_description = "Email"
    usuario__telefono.short_description = "Teléfono"

admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Servicio)
admin.site.register(Categoria)
