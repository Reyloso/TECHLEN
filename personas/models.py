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

    Id_Persona = models.CharField(max_length=10, primary_key=True)
    Primer_Nombre = models.CharField(max_length=30, null=True)
    Segundo_Nombre = models.CharField(max_length=30, null=True)
    Primer_Apellido = models.CharField(max_length=30, null=True)
    Segundo_Apellido = models.CharField(max_length=30, null=True)
    Nro_Documento = models.CharField(max_length=30)
    Tipo_Documento = models.CharField(max_length=30, choices=TIPO_NID)
    Correo_Institucional = models.EmailField(max_length=50, unique=True)
    Nro_Telefonico = models.CharField(max_length=30, null=True)

class Tipo_persona(models.Model):
    TIPO_PERSONA = (
        ('ESTUDIANTE', 'ESTUDIANTE'),
        ('PROFESOR', 'PROFESOR'),
        ('ADMINISTRATIVO', 'ADMINISTRATIVO'),
    )

    tipo_persona = models.CharField(max_length=30,choices=TIPO_PERSONA)
    Id_Persona = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.tipo_persona)

class Estudiantes(Personas):
    GENERO_ESTUDIANTE = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    class Meta:
        verbose_name_plural = "Estudiantes"

    foto_url = models.URLField(null=True)
    genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
    Programa_Academico = models.ForeignKey(Programa, null=True)
    Ciclo_Lectivo = models.CharField(max_length=30, null=True)
    Descripcion = models.CharField(max_length=30, null=True)

    def nombre_completo(self):
        return self.Primer_Nombre + " " + self.Segundo_Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido

    class Estudiantes(Personas):
        GENERO_ESTUDIANTE = (
            ('F', 'Femenino'),
            ('M', 'Masculino'),
        )

        class Meta:
            verbose_name_plural = "Estudiantes"

        genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
        Programa_Academico = models.ForeignKey(Programa, null=True)
        Ciclo_Lectivo = models.CharField(max_length=30, null=True)
        Descripcion = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return unicode(self.Primer_Nombre + " " + self.Segundo_Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido)

