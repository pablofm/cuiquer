# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20161108_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='preguntas_especificas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
