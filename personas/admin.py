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

	Programa_Academico = fields.Field(attribute='Programa_Academico',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	class Meta:
		import_id_fields = ('Nro_Tarjeta',)
		model = Personas
		export_order = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')
		fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')


class Persona (ImportExportModelAdmin):
	# def has_delete_permission(self, request, obj=None):
	# 	return False

	def add_view(self, *args, **kwargs):
		self.fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')
		return super(Persona, self).add_view(*args, **kwargs)

	def change_view(self, *args, **kwargs):
		self.fields = ('Nro_Tarjeta','Tipo_Documento','Nro_Documento','Estado_tarjeta')
		return super(Persona, self).change_view(*args, **kwargs)

	def reporte_prestamos(self, instance):
		return "<a href='/admin/Persona/Reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Id_Persona

	reporte_prestamos.short_description = "Reporte Persona"
	reporte_prestamos.allow_tags = True
	reporte_prestamos.is_column = True

	list_display = ['Nro_Tarjeta','Id_Persona','nombre_completo','Tipo_Documento','Nro_Documento','Correo_Institucional','Programa_Academico','Estado_tarjeta', 'Tipo_Persona','reporte_prestamos']
	list_filter = ['Programa_Academico','Estado_tarjeta','Ciclo_Lectivo']
	search_fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento')
	resource_class = PersonaResource
	class Meta:
		model = Personas

admin.site.register(Personas,Persona)
