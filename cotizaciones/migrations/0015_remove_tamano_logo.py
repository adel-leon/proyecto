# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0014_auto_20171116_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tamano',
            name='logo',
        ),
    ]
