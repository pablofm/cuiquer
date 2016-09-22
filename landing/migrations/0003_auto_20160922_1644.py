# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='fecha_alta',
            field=models.DateTimeField(auto_now=True),
        ),
    ]