from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Programa(models.Model):
    cod = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Programas"

    def __unicode__(self):
        return unicode(self.nombre)
