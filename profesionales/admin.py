from django.contrib import admin
from profesionales.models import Profesional, Servicio, Categoria
from perfiles.models import Usuario


class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('usuario__nombre', 'usuario__email')
    list_filter = ['servicios']

    def usuario__nombre(self, obj):
        return obj.usuario.nombre

    def usuario__email(self, obj):
        return obj.usuario.email

admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Servicio)
admin.site.register(Categoria)
