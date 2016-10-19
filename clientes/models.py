from django.db import models
from profesionales.models import Servicio
from perfiles.models import Usuario


class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario)
    servicio = models.ForeignKey(Servicio, related_name='clientes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(null=True, blank=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)
