# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0013_remove_tamano_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='relleno',
            name='logo',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tamano',
            name='logo',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]