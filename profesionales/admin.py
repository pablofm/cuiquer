from django import forms
from django.contrib import admin
from clientes.fields import GroupedModelMultiChoiceField

from profesionales.models import Profesional, Servicio  # ,categoria
from perfiles.admin import UsuarioModelAdmin


class ProfesionalAdminForm(forms.ModelForm):
    servicios = GroupedModelMultiChoiceField(
        queryset=Servicio.objects.all(),
        group_by_field='categoria')

    class Meta:
        model = Profesional
        fields = '__all__'


class ProfesionalAdmin(UsuarioModelAdmin):
    form = ProfesionalAdminForm

    list_display = ('nombre', 'email', 'telefono', 'codigo_postal', 'fecha_ultima_modificacion')
    list_filter = ['servicios']

    readonly_fields = ('fecha_alta', 'fecha_ultima_modificacion', 'origen', 'detalles_usuario')

    fieldsets = (
        ('Datos Básicos', {
           'fields': ('detalles_usuario', 'fecha_alta', 'fecha_ultima_modificacion', 'origen', 'fecha_nacimiento', 'codigo_postal')
        }),
        ('Datos Profesionales', {
            'fields': ('servicios', 'metodo_trabajo', 'precio'),
        }),
        ('Enlaces', {
            'fields': ('facebook', 'linkedin'),
        }),
        ('Información extra', {
            'fields': ('formacion_relacionada', 'opiniones_clientes', 'observaciones'),
        }),
    )

    class Meta:
        model = Profesional

admin.site.register(Profesional, ProfesionalAdmin)
# admin.site.register(Servicio)
# admin.site.register(Categoria)
