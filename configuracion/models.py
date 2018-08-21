from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Programa(models.Model):
    cod = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60,null=False)

    class Meta:
        verbose_name_plural = "Dependencia"

    def __unicode__(self):
        return unicode(self.nombre)

# class Cargo(models.Model):
#     cod = models.AutoField(primary_key=True)
#     Cargo = models.CharField(max_length=60)
#
#     class Meta:
#         verbose_name_plural = "Cargos"
#
#     def __unicode__(self):
#         return unicode(self.Cargo)

# class Dependencia(models.Model):
#     cod = models.AutoField(primary_key=True)
#     Dependencia = models.CharField(max_length=60)
#
#     class Meta:
#         verbose_name_plural = "Dependencias"
#
#     def __unicode__(self):
#         return unicode(self.Dependencia)
