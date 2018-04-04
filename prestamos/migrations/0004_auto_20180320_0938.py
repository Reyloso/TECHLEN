# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 14:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_detalle_prestamo_incidente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='id',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='id_prestamo',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]