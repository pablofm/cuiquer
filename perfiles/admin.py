from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from perfiles.models import Usuario
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class UsuarioModelAdmin(admin.ModelAdmin):
    def nombre(self, obj):
        return obj.usuario.nombre

    def email(self, obj):
        return obj.usuario.email

    def telefono(self, obj):
        return obj.usuario.telefono

    def detalles_usuario(self, obj):
        return mark_safe('Nombre: {}<br>Email: {}<br>Teléfono: {}<br><a href="{}">Editar</a>'.format(
            self.nombre(obj),
            self.email(obj),
            self.telefono(obj),
            reverse("admin:perfiles_usuario_change", args=(obj.usuario.pk,))))
    nombre.short_description = "Nombre"
    email.short_description = "Email"
    telefono.short_description = "Teléfono"
    readonly_fields = ('nombre', 'email', 'telefono', 'detalles_usuario')


class UsuarioAdmin(BaseUserAdmin):
    empty_value_display = '???'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_filter = ('is_admin',)
    list_display = ('nombre', 'email', 'telefono', 'is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('nombre', 'email', 'telefono', 'foto', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = ((None, {
            'classes': ('wide',),
            'fields': ('nombre', 'email', 'telefono', 'foto', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Usuario, UsuarioAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
