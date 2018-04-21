from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.timezone import now

class Tipo_Recurso(models.Model):

    class Meta:
        verbose_name_plural = "Tipo De Recursos"

    id_recurso = models.CharField(max_length=40, primary_key=True)
    tipo_recurso = models.CharField(max_length=30, null=True)
    def __unicode__(self):
        return unicode(str(self.tipo_recurso))

class Recurso(models.Model):

    class Meta:
        verbose_name_plural = "Recursos"

    Id_recurso = models.AutoField(primary_key=True)
    tipo_de_recurso = models.ForeignKey(Tipo_Recurso, null=True)
    nombre_recurso = models.CharField(max_length=30, null=True)
    referencia = models.CharField(max_length=40)
    fecha_registro = models.DateField(default=now)
    fecha_de_baja = models.DateField(blank=True)

    def __unicode__(self):
        return unicode(str(self.nombre_recurso))


class Incidente(models.Model):
    ESTADO = (
        ('EN REVISION', 'EN REVISION'),
        ('ACEPTADO', 'ACEPTADO'),
        ('DADO DE BAJA', 'DADO DE BAJA'),
    )


    class Meta:
        verbose_name_plural = "Registo De Incidentes"

    Id_Incidente = models.AutoField(primary_key=True)    
    recurso = models.ForeignKey(Recurso, null=True)
    Fecha_Incidente = models.DateField(default=now)
    descripcion = models.TextField(null=True)
    Estado= models.CharField(max_length=30, choices=ESTADO)

    def __unicode__(self):
        return unicode(str(self.recurso))
