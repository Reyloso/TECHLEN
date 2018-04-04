# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from configuracion.models import *

# Create your models here.
class Personas(models.Model):
    TIPO_NID = (
        ('TI', 'TI'),
        ('CC', 'CC'),
    )
    GENERO_ESTUDIANTE = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    SEDE = (
        ('Apartado', 'Apartado'),
        ('Arauca', 'Arauca'),
        ('Barrancabermeja', 'Barrancabermeja'),
        ('Bogota', 'Bogota'),
        ('Bucaramanga', 'Bucaramanga'),
        ('Cali', 'Cali'),
        ('Monteria', 'Monteria'),
        ('Medellin', 'Medellin'),
    )
    Nro_Tarjeta = models.CharField(max_length=10, null=True)
    Id_Persona = models.CharField(max_length=10, primary_key=True)
    Primer_Nombre = models.CharField(max_length=30, null=True)
    Segundo_Nombre = models.CharField(max_length=30, null=True)
    Primer_Apellido = models.CharField(max_length=30, null=True)
    Segundo_Apellido = models.CharField(max_length=30, null=True)
    Tipo_Documento = models.CharField(max_length=30, choices=TIPO_NID)
    Nro_Documento = models.CharField(max_length=30)
    Sede = models.CharField(max_length=30, choices=SEDE, null=True)
    Codigo_ops = models.CharField(max_length=20, null=True)
    genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
    Correo_Institucional = models.EmailField(max_length=50, unique=True)
    Formato_credencial = models.CharField(max_length=20, null=True)
    Grupo_acceso = models.CharField(max_length=20, null=True)
    Estado_tarjeta = models.CharField(max_length=20, null=True)
    foto_url = models.URLField(null=True)


class Tipo_persona(models.Model):
    TIPO_PERSONA = (
        ('ESTUDIANTE', 'ESTUDIANTE'),
        ('PROFESOR O ADMINISTRATIVO', 'PROFESOR O ADMINISTRATIVO'),
    )

    tipo_persona = models.CharField(max_length=30,choices=TIPO_PERSONA)
    Id_Persona = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.tipo_persona)

class Estudiantes(Personas):

    Programa_Academico = models.ForeignKey(Programa, null=True)
    Ciclo_Lectivo = models.CharField(max_length=30, null=True)
    class Meta:
        verbose_name_plural = "Estudiantes"

    def __unicode__(self):
        return unicode(self.Primer_Nombre + " " + self.Segundo_Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido)

class Profesores_Administrativos(Personas):

    Cargo = models.CharField(max_length=30, null=True)
    Dependencia = models.CharField(max_length=30, null=True)
    class Meta:
        verbose_name_plural = "Profesores o Administrativos"

    def __unicode__(self):
        return unicode(self.Primer_Nombre + " " + self.Segundo_Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido)
