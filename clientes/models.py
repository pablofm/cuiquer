from django.db import models
from profesionales.models import Servicio
from django.conf import settings
from profesionales.models import METODO_TRABAJO_CHOICES, ORIGEN_CHOICES

CONTACTO_CHOICES = (
    ('1', 'Prefiero Llamar'),
    ('2', 'Prefiere que me llamen'),
)


class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    servicio = models.ForeignKey(Servicio, related_name='clientes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)
    metodo_trabajo = models.CharField(max_length=1, choices=METODO_TRABAJO_CHOICES, blank=True, null=True)
    metodo_contacto = models.CharField(max_length=1, choices=CONTACTO_CHOICES, blank=True, null=True)
    donde = models.CharField(max_length=100, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    origen = models.CharField(max_length=2, choices=ORIGEN_CHOICES, blank=True, null=True)
    informacion_extra = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    preguntas_especificas = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.usuario)
