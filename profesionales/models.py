from django.db import models


class Trabajo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    nombre_cliente = models.CharField(max_length=100)
    contacto_cliente = models.CharField(max_length=100)
    recomendacion_cliente = models.TextField()
    profesional = models.ForeignKey('Profesional', related_name='trabajos')


class Profesional(models.Model):
    servicio = models.CharField(max_length=100)

    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    lugar_de_residencia = models.CharField(max_length=30)
    radio_prestacion = models.IntegerField()

    # Campos opcionales
    web = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    nombre_empresa = models.CharField(max_length=100, blank=True)

    # Preguntas basicas
    como = models.TextField()
    que = models.TextField()
    experiencia = models.TextField()

    # Preguntas adicinales
    consejo = models.TextField(blank=True)
    formacion = models.TextField(blank=True)
    tipo_cliente = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
