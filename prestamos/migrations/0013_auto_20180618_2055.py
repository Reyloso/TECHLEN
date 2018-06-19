# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 01:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0012_incidente_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleprestamo',
            name='Usuario_devolucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
