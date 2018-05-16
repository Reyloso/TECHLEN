# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('Id_Incidente', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Incidente', models.DateField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(null=True)),
                ('Estado', models.CharField(choices=[('EN REVISION', 'EN REVISION'), ('ACEPTADO', 'ACEPTADO'), ('DADO DE BAJA', 'DADO DE BAJA')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Registo De Incidentes',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('Id_recurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_recurso', models.CharField(max_length=20, null=True)),
                ('referencia', models.CharField(max_length=10)),
                ('Estado_Recurso', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('PRESTADO', 'PRESTADO'), ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'), ('DADO DE BAJA', 'DADO DE BAJA')], max_length=20)),
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Recurso',
            fields=[
                ('id_recurso', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('tipo_recurso', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipo De Recursos',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo_de_recurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Tipo_Recurso'),
        ),
        migrations.AddField(
            model_name='incidente',
            name='Recurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Recurso'),
        ),
    ]
