from django.db import models
from profesionales.models import Servicio
from django.conf import settings


class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    servicio = models.ForeignKey(Servicio, related_name='clientes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(null=True, blank=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return str(self.usuario)
