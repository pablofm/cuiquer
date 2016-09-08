from django.db import models
from profesionales.models import Servicio
from django.urls import reverse


class Cliente(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='clientes')
    fecha_solicitud = models.DateField(auto_now_add=True)
    nombre_cliente = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('cliente-detail', kwargs={'cliente_id': self.pk})
