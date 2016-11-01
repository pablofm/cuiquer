from django import forms
from django.contrib import admin
from clientes.fields import GroupedModelMultiChoiceField

from profesionales.models import Profesional, Servicio, Categoria
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

    empty_value_display = '???'
    list_display = ('nombre', 'email', 'telefono', 'codigo_postal', 'fecha_ultima_modificacion')
    list_filter = ['servicios']
    readonly_fields = ('fecha_alta', 'fecha_ultima_modificacion', 'origen', 'detalles_usuario')
    fields = (
        'fecha_alta', 'fecha_ultima_modificacion', 'detalles_usuario', 'servicios',
        'fecha_nacimiento', 'codigo_postal', 'metodo_trabajo', 'precio',
        'facebook', 'linkedin', 'formacion_relacionada', 'opiniones_clientes',
        'observaciones', 'origen')


admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Servicio)
admin.site.register(Categoria)
