from django.contrib import admin
from landing.models import Contacto, Suscripcion


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha')
    readonly_fields = ('fecha',)


class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ('email', 'fecha_alta')
    readonly_fields = ('fecha_alta',)

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)
