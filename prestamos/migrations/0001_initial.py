# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 19:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0001_initial'),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleIncidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(null=True)),
                ('Fecha', models.DateField(null=True)),
                ('Hora', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'detalle incidencias',
            },
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('Id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_prestamo', models.DateField(default=django.utils.timezone.now)),
                ('Estado', models.CharField(choices=[('PRESTADO', 'PRESTADO'), ('DEVUELTO', 'DEVUELTO'), ('PERDIDO', 'PERDIDO')], default='PRESTADO', max_length=20)),
                ('Fecha_devolucion', models.DateField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Detalle Prestamos',
            },
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('Id_Incidente', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo_Incidente', models.CharField(choices=[('INCIDENTE TOTAL DEL RECURSO', 'INCIDENTE TOTAL DEL RECURSO'), ('INCIDENTE PARCIAL DEL RECURSO', 'INCIDENTE PARCIAL DEL RECURSO'), ('PERDIDA DEL RECURSO', 'PERDIDA DEL RECURSO'), ('OTRO', 'OTRO')], max_length=50)),
                ('Fecha_Incidente', models.DateField(default=django.utils.timezone.now)),
                ('Estado', models.CharField(choices=[('EN REVISION', 'EN REVISION'), ('REVISADO', 'REVISADO')], max_length=30)),
                ('Persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Personas')),
                ('Prestamo_detalle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prestamos.DetallePrestamo')),
                ('Recurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Recurso')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Registo De Incidentes',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('Id_prestamo', models.AutoField(primary_key=True, serialize=False)),
                ('Estado_prestamo', models.CharField(choices=[('EN CURSO', 'EN CURSO'), ('DEVUELTO', 'DEVUELTO')], max_length=20)),
                ('Fecha_prestamo', models.DateField(default=django.utils.timezone.now)),
                ('Hora_prestamo', models.TimeField(default=django.utils.timezone.now)),
                ('Fecha_devolucion', models.DateField(blank=True, null=True)),
                ('Hora_devolucion', models.TimeField(blank=True, null=True)),
                ('Persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Personas')),
                ('Usuario_Prestatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Prestamos',
            },
        ),
        migrations.AddField(
            model_name='detalleprestamo',
            name='Prestamo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prestamos.Prestamo'),
        ),
        migrations.AddField(
            model_name='detalleprestamo',
            name='Recurso_detalle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Recurso'),
        ),
        migrations.AddField(
            model_name='detalleprestamo',
            name='Usuario_devolucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detalleincidente',
            name='Incidente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prestamos.Incidente'),
        ),
        migrations.AddField(
            model_name='detalleincidente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
