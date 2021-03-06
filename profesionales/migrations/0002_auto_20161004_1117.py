# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 11:17
from __future__ import unicode_literals

from django.db import migrations


def servicios_iniciales(apps, schema_editor):
    Servicio = apps.get_model("profesionales", "Servicio")
    Categoria = apps.get_model("profesionales", "Categoria")

    salud_y_bienestar = Categoria.objects.create(nombre_categoria='Salud y bienestar')
    Servicio.objects.create(categoria=salud_y_bienestar, nombre_servicio='Fisioterapeuta')
    Servicio.objects.create(categoria=salud_y_bienestar, nombre_servicio='Osteópata')
    Servicio.objects.create(categoria=salud_y_bienestar, nombre_servicio='Masajista')
    Servicio.objects.create(categoria=salud_y_bienestar, nombre_servicio='Peluquería')
    Servicio.objects.create(categoria=salud_y_bienestar, nombre_servicio='Maquillaje')

    cuidado_de_personas = Categoria.objects.create(nombre_categoria='Cuidado de personas')
    Servicio.objects.create(categoria=cuidado_de_personas, nombre_servicio='Cuidado de niños (canguro)')
    Servicio.objects.create(categoria=cuidado_de_personas, nombre_servicio='Cuidado de ancianos ')

    clases_particulares = Categoria.objects.create(nombre_categoria='Clases particulares')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Primaria')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Secundaria')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Bachillerato')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='informática')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Inglés')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Francés')
    Servicio.objects.create(categoria=clases_particulares, nombre_servicio='Mindfullness')

    deportes = Categoria.objects.create(nombre_categoria='Deportes')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Entrenador Personal')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Monitor de Tenis')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Monitor de Pádel')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Monitor de Natación')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Profesor de Yoga')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Profesor de Pilates')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Coach')
    Servicio.objects.create(categoria=deportes, nombre_servicio='Nutricionista')

    hogar_y_limpieza = Categoria.objects.create(nombre_categoria='Hogar y limpieza')
    Servicio.objects.create(categoria=hogar_y_limpieza, nombre_servicio='Limpieza del hogar')
    Servicio.objects.create(categoria=hogar_y_limpieza, nombre_servicio='Limpieza de oficinas')
    Servicio.objects.create(categoria=hogar_y_limpieza, nombre_servicio='Empresa de limpieza')
    Servicio.objects.create(categoria=hogar_y_limpieza, nombre_servicio='Limpieza de vehículos')
    Servicio.objects.create(categoria=hogar_y_limpieza, nombre_servicio='Jardinero')

    servicios_informaticos = Categoria.objects.create(nombre_categoria='Servicios informáticos')
    Servicio.objects.create(categoria=servicios_informaticos, nombre_servicio='Diseño de páginas web')
    Servicio.objects.create(categoria=servicios_informaticos, nombre_servicio='Diseño de logos')
    Servicio.objects.create(categoria=servicios_informaticos, nombre_servicio='Instalación de ordenadores')
    Servicio.objects.create(categoria=servicios_informaticos, nombre_servicio='Reparación de ordenadores')

    reparaciones_y_reformas = Categoria.objects.create(nombre_categoria='Reparaciones y reformas')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Albañil')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Fontanero')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Electricista')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Carpintero')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Pintor')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Reparación de electrodomésticos')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Interiorista')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Aparejador')
    Servicio.objects.create(categoria=reparaciones_y_reformas, nombre_servicio='Empresa de reformas')


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(servicios_iniciales),
    ]
