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
class PersonaResource(resources.ModelResource):

	class Meta:
		import_id_fields = ('Nro_Tarjeta',)
		model = Personas
		export_order = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')
		fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')


class Persona (ImportExportModelAdmin):
    list_display = ['Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona']
    list_filter = ['Programa_Academico','Estado_tarjeta','Ciclo_Lectivo' ]
    search_fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento')
    resource_class = PersonaResource

    class Meta:
		model = Personas

admin.site.register(Personas,Persona)
