# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_solicitud',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
