# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0002_auto_20160926_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesional',
            old_name='servicio',
            new_name='servicios',
        ),
    ]
