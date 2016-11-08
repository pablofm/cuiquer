from django.db import models
from django.conf import settings
import uuid


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    preguntas_especificas = models.TextField(default='Por definir')

    def __str__(self):
        return str(self.nombre_categoria)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre_categoria']


class Servicio(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_servicio)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['categoria', 'nombre_servicio']


METODO_TRABAJO_CHOICES = (
    ('a', 'Autónomo'),
    ('e', 'Empresa'),
    ('p', 'Particular'),
)


ORIGEN_CHOICES = (
    ('am', 'Amigo'),
    ('em', 'Email'),
    ('bu', 'Buscador'),
    ('fa', 'Facebook'),
    ('tw', 'Twitter'),
    ('in', 'Instagram'),
    ('mi', 'Milanuncios'),
    ('jo', 'JobToday'),
    ('ot', 'Otros')
)


class Profesional(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    codigo_postal = models.CharField(max_length=5)
    metodo_trabajo = models.CharField(max_length=1, choices=METODO_TRABAJO_CHOICES, blank=True, null=True)
    origen = models.CharField(max_length=2, choices=ORIGEN_CHOICES, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    formacion_relacionada = models.TextField(null=True, blank=True)
    opiniones_clientes = models.TextField(null=True, blank=True)
    servicios = models.ManyToManyField(Servicio)
    observaciones = models.TextField(null=True, blank=True)
    codigo_actualizacion = models.UUIDField(default=uuid.uuid4, blank=True, null=True, editable=True)

    def __str__(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
