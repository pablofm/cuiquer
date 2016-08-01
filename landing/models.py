from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()


class NewsLetter(models.Model):
    email = models.EmailField()
