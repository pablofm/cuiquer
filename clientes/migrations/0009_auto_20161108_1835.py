# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20161108_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cuestionario',
        ),
        migrations.DeleteModel(
            name='CuestionarioExtra',
        ),
    ]
