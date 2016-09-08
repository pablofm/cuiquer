from django.db import models
from django.urls import reverse


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_servicio)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nombre_servicio']


class Profesional(models.Model):
    servicio = models.ManyToManyField(Servicio)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    area_servicio = models.CharField(max_length=30)

    # Preguntas basicas
    que = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profesional-detail', kwargs={'profesional_id': self.pk})

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
