from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from personas.models import Personas
from recursos.models import Recurso
from django.contrib.auth.models import User

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
    Usuario_Prestatario = models.ForeignKey(User)
    Persona = models.ForeignKey(Personas, null=True)
    recurso = models.ManyToManyField(Recurso, null=True)
    Estado_prestamo = models.CharField(max_length=20, choices=ESTADO)
    Fecha_prestamo = models.DateField(default=now)
    Hora_prestamo = models.TimeField(default=now)
    Fecha_devolucion = models.DateField(blank=True, null=True)
    Hora_devolucion = models.TimeField(blank=True, null=True)

    def get_recurso(self):
       return ",".join([r.nombre_recurso for r in self.recurso.all()])
    get_recurso.short_description = 'recurso'
    get_recurso.allow_tags = True

    def __unicode__(self):
        return unicode(str(self.Id_prestamo))


class Incidente(models.Model):
    ESTADO = (
        ('EN REVISION', 'EN REVISION'),
        ('ACEPTADO', 'ACEPTADO'),
        ('DADO DE BAJA', 'DADO DE BAJA'),
    )

    class Meta:
        verbose_name_plural = "Registo De Incidentes"

    Id_Incidente = models.AutoField(primary_key=True)
    Fecha_Incidente = models.DateField(default=now)
    Recurso = models.ForeignKey(Recurso, null=True)
    Prestamo = models.ForeignKey(Prestamo, null=True)
    descripcion = models.TextField(null=True)
    Estado= models.CharField(max_length=30, choices=ESTADO)

    def __unicode__(self):
        return unicode(str(self.descripcion))
