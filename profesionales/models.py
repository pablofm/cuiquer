from django.db import models
from perfiles.models import Usuario


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_categoria)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nombre_categoria']


class Servicio(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_servicio)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['categoria']


class Profesional(models.Model):
    usuario = models.ForeignKey(Usuario)
    servicios = models.ManyToManyField(Servicio)
    codigo_postal = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
