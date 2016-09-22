from django.db import models


class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.email)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class Suscripcion(models.Model):
    fecha_alta = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return '{} - {}'.format(self.fecha_alta, self.email)

    class Meta:
        verbose_name = 'Suscripción'
        verbose_name_plural = 'Suscripciones'
