# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0009_auto_20171115_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aditivospan',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='cubierta',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='relleno',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='logo',
        ),
        migrations.AddField(
            model_name='tamano',
            name='logo',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
