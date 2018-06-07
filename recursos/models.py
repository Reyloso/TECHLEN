from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from prestamos.models import *

class Tipo_Recurso(models.Model):

    class Meta:
        verbose_name_plural = "Tipo De Recursos"

    id_recurso = models.CharField(max_length=40, primary_key=True)
    tipo_recurso = models.CharField(max_length=30, null=True)
    def __unicode__(self):
        return unicode(str(self.tipo_recurso))

class Recurso(models.Model):
    ESTADO = (
        ('ACTIVO', 'ACTIVO'),
        ('PRESTADO', 'PRESTADO'),
        ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'),
        ('DADO DE BAJA', 'DADO DE BAJA'),
    )
    class Meta:
        verbose_name_plural = "Recursos"

    Id_recurso = models.AutoField(primary_key=True,editable=False)
    tipo_de_recurso = models.ForeignKey(Tipo_Recurso, null=True)
    nombre_recurso = models.CharField(max_length=100, null=True)
    referencia = models.CharField(max_length=100)
    Estado_Recurso = models.CharField(max_length=20, choices=ESTADO,default="ACTIVO")
    fecha_registro = models.DateField(default=now,editable=False)

    def __unicode__(self):
        return unicode(str(self.nombre_recurso))
