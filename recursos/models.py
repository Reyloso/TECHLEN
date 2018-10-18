# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from prestamos.models import *

class TipoRecurso(models.Model):

    class Meta:
        verbose_name_plural = "Tipo De Recursos"

    tipo_recurso = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.tipo_recurso)

class Marca(models.Model):

    class Meta:
        verbose_name_plural = "Marca"

    Marca = models.CharField(max_length=60, null=True)
    def __str__(self):
        return str(self.Marca)


class Recurso(models.Model):
    ESTADO = (
        ('ACTIVO', 'ACTIVO'),
        ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'),
        ('DADO DE BAJA POR PERDIDA', 'DADO DE BAJA POR PERDIDA'),
        ('DADO DE BAJA POR DAÑO TOTAL', 'DADO DE BAJA POR DAÑO TOTAL'),
    )
    class Meta:
        verbose_name_plural = "Recursos"

    tipo_de_recurso = models.ForeignKey(TipoRecurso, null=True)
    Marca = models.ForeignKey(Marca, null=True)
    nombre_recurso = models.CharField(max_length=100, null=True)
    Numero_Serie = models.CharField(max_length=100, null=True,blank=True)
    referencia = models.CharField(max_length=100)
    Estado_Recurso = models.CharField(max_length=40, choices=ESTADO,default="ACTIVO")
    fecha_registro = models.DateField(default=now)

    def __str__(self):
        return str(self.nombre_recurso)
