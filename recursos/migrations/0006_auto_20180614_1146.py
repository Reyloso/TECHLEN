# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0005_auto_20180612_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='Estado_Recurso',
            field=models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'), ('DADO DE BAJA', 'DADO DE BAJA')], default='ACTIVO', max_length=20),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='Id_recurso',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='fecha_registro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
