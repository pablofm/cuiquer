# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='codigo_postal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
