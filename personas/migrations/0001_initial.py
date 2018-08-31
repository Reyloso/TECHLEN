# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoAcceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nro_Tarjeta', models.CharField(max_length=50, unique=True)),
                ('Nro_Documento', models.CharField(max_length=80)),
                ('Nombres', models.CharField(max_length=80)),
                ('Apellidos', models.CharField(max_length=80)),
                ('Estado_Tarjeta', models.CharField(choices=[('ACTIVA', 'ACTIVA'), ('INACTIVA', 'INACTIVA')], max_length=30)),
                ('Codigo_Acceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.CodigoAcceso')),
                ('Dependencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracion.Programa')),
            ],
            options={
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_persona', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='personas',
            name='Tipo_Persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.TipoPersona'),
        ),
    ]
