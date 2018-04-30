# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from configuracion.models import *

# Register your models here.
class Estudiante (admin.ModelAdmin):
    list_display = ['Nro_Tarjeta','Id_Persona','nombre_completo','Nro_Documento','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta']
    list_filter = ['Programa_Academico','Estado_tarjeta','Ciclo_Lectivo' ]
    search_fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento')

    class Meta:
		model = Estudiantes

class Profesores_Administrativo (admin.ModelAdmin):
    list_display = ['Nro_Tarjeta','Id_Persona','nombre_completo','Nro_Documento','Correo_Institucional','Dependencia','Cargo','Estado_tarjeta']
    list_filter = ['Dependencia','Estado_tarjeta','Cargo' ]
    search_fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Dependencia')

    class Meta:
		model = Estudiantes


admin.site.register(Estudiantes,Estudiante),
admin.site.register(Profesores_Administrativos,Profesores_Administrativo),
