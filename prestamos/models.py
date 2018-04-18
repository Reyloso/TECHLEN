from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from personas.models import *
from recursos.models import *

# Create your models here.
class Prestamo(models.Model):

    class Meta:
        verbose_name_plural = "Prestamos"

    id_prestamo = models.CharField(max_length=10, primary_key=True)
    ID_Persona = models.ForeignKey(Estudiantes, null=True)
    Fecha_prestamo = models.DateField(default=now)
    Fecha_devolucion = models.DateField(null=True)

    def __unicode__(self):
        return unicode(str(self.id_prestamo) + " " + str(self.ID_Persona))

class Incidencia(models.Model):

    class Meta:
        verbose_name_plural = "Incidencias"

    Fecha_Incidencia = models.DateField(default=now)
    def __unicode__(self):
        return unicode(str(self.Fecha_Incidencia))

class Detalle_Prestamo(models.Model):

    class Meta:
        verbose_name_plural = "Detalle Prestamos"

    recurso = models.ForeignKey(Recurso, null=True)
    prestamo =  models.ForeignKey(Prestamo, null=True)
    Incidente = models.ForeignKey(Incidencia, null=True)

    def __unicode__(self):
        return unicode(self.id)
