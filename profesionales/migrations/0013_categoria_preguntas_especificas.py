# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0012_auto_20161108_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='preguntas_especificas',
            field=models.TextField(default='Por definir'),
        ),
    ]