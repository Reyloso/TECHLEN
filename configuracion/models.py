from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Programa(models.Model):
    cod = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60,null=False)

    class Meta:
        verbose_name_plural = "Dependencia"

    def __str__(self):
        return str(self.nombre)
