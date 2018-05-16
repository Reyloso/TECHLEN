from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from personas.models import *
from recursos.models import *

# Create your models here.
class Prestamo(models.Model):
    ESTADO = (
        ('EN CURSO', 'EN CURSO'),
        ('EN REVISION', 'EN REVISION'),
        ('DEVUELTO', 'DEVUELTO'),
    )

    class Meta:
        verbose_name_plural = "Prestamos"

    Id_prestamo = models.AutoField(primary_key=True)
    Persona = models.ForeignKey(Personas, null=True)
    recurso = models.ManyToManyField(Recurso, null=True)
    Estado_prestamo = models.CharField(max_length=20, choices=ESTADO)
    Fecha_prestamo = models.DateField(default=now)
    Hora_prestamo = models.TimeField(null=True)
    Fecha_devolucion = models.DateField(blank=True, null=True)
    Hora_devolucion = models.TimeField(blank=True, null=True)

    def get_recurso(self):
       return ",".join([r.nombre_recurso for r in self.recurso.all()])
    get_recurso.short_description = 'recurso'
    get_recurso.allow_tags = True

    def __unicode__(self):
        return unicode(str(self.Id_prestamo) + " " + str(self.Persona))
