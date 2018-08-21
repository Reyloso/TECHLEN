#!/usr/bin/env python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from django.db import models
from configuracion.models import Programa

# Create your models here.

class CodigoAcceso(models.Model):
    Codigo = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return unicode (self.Codigo)

class TipoPersona(models.Model):
    Tipo_persona = models.CharField(max_length=50, null=True)
    def __unicode__(self):
        return unicode (self.Tipo_persona)

class Personas(models.Model):

    ESTADO_TARJETA = (
        ('ACTIVA', 'ACTIVA'),
        ('INACTIVA', 'INACTIVA'),
    )
    Nro_Tarjeta = models.CharField(max_length=10, null=False, unique=True, primary_key=True)
    Nro_Documento = models.CharField(max_length=80,null=False)
    Nombres = models.CharField(max_length=80)
    Apellidos = models.CharField(max_length=80)
    Estado_Tarjeta = models.CharField(max_length=30, choices=ESTADO_TARJETA)
    Tipo_Persona = models.ForeignKey(TipoPersona, null=True)
    Dependencia = models.ForeignKey(Programa, null=True)
    Codigo_Acceso = models.ForeignKey(CodigoAcceso, null=True)
    # Correo_Institucional = models.EmailField(max_length=50, unique=True)
    # Id_Persona = models.CharField(max_length=10, unique=True)
    # Primer_Nombre = models.CharField(max_length=30, null=True)
    # Segundo_Nombre = models.CharField(max_length=30,blank=True, null=True)
    # Primer_Apellido = models.CharField(max_length=30, null=True)
    # Segundo_Apellido = models.CharField(max_length=30,blank=True, null=True)
    # Tipo_Documento = models.CharField(max_length=30, choices=TIPO_NID)
    # Sede = models.CharField(max_length=30, choices=SEDE, null=True)
    # genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
    # Ciclo_Lectivo = models.CharField(max_length=30, null=True)
    # Cargo = models.ManyToManyField(Cargo, blank=True, null=False)
    # Dependencias = models.ForeignKey(Dependencia,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Personas"

    def __unicode__(self):
        return unicode(self.Nro_Tarjeta)
