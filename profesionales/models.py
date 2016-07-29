from django.db import models


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_servicio)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class Profesional(models.Model):
    servicio = models.ManyToManyField(Servicio)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    area_servicio = models.CharField(max_length=30)

    # Preguntas basicas
    que = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'


class Trabajo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    nombre_cliente = models.CharField(max_length=100)
    contacto_cliente = models.CharField(max_length=100)
    recomendacion_cliente = models.TextField()
    profesional = models.ForeignKey('Profesional', related_name='trabajos')

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
