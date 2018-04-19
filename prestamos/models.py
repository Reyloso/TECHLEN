from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from personas.models import *
from recursos.models import *

# Create your models here.
class Prestamo(models.Model):

    class Meta:
        verbose_name_plural = "Prestamos"

    Id_prestamo = models.CharField(max_length=5, primary_key=True)
    Persona = models.ForeignKey(Estudiantes, null=True)
    recurso = models.ManyToManyField(Recurso, null=True)
    Fecha_prestamo = models.DateField(default=now)
    Fecha_devolucion = models.DateField(null=True)

    def __unicode__(self):
        return unicode(str(self.Id_prestamo) + " " + str(self.Persona))
