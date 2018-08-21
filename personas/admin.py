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

class CodigoAccesos (admin.ModelAdmin):
        list_display = ['id','Codigo']
        class Meta:
		          model = CodigoAcceso

class TipoPersonas (admin.ModelAdmin):
        list_display = ['id','Tipo_persona']
        class Meta:
		          model = TipoPersona


class PersonaResource(resources.ModelResource):

	Dependencia = fields.Field(attribute='Dependencia',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	Tipo_Persona = fields.Field(attribute='Tipo_Persona',
								   widget=ForeignKeyWidget(TipoPersona, 'Tipo_persona'))

	Codigo_Acceso = fields.Field(attribute='Codigo_Acceso',
								   widget=ForeignKeyWidget(CodigoAcceso, 'Codigo'))


	class Meta:
		import_id_fields = ('Nro_Tarjeta',)
		model = Personas
		export_order = ('Apellidos','Nombres','Dependencia','Nro_Tarjeta','Tipo_Persona','Codigo_Acceso','Estado_Tarjeta','Nro_Documento')
		fields =  ('Nro_Tarjeta','Nro_Documento','Nombres','Apellidos','Estado_Tarjeta','Tipo_Persona','Dependencia','Codigo_Acceso')


class Persona (ImportExportModelAdmin):
    list_per_page = 40
	# def has_delete_permission(self, request, obj=None):
	# 	return False

	# def add_view(self, *args, **kwargs):
	# 	self.fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Programa_Academico','Ciclo_Lectivo','Estado_tarjeta', 'Tipo_Persona')
	# 	return super(Persona, self).add_view(*args, **kwargs)
	#
	# def change_view(self, *args, **kwargs):
	# 	self.fields = ('Nro_Tarjeta','Tipo_Documento','Nro_Documento','Estado_tarjeta')
	# 	return super(Persona, self).change_view(*args, **kwargs)
    def reporte_prestamos(self, instance):
		return "<a href='/admin/persona/Reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Nro_Tarjeta

    reporte_prestamos.short_description = "Reporte Persona"
    reporte_prestamos.allow_tags = True
    reporte_prestamos.is_column = True

    list_display = ['Nro_Tarjeta','Nro_Documento','Nombre_Completo','Estado_Tarjeta','Tipo_Persona','Dependencia','Codigo_Acceso','reporte_prestamos']
    list_filter = ['Dependencia','Estado_Tarjeta','Tipo_Persona','Codigo_Acceso']
    search_fields = ('Nro_Tarjeta','Nro_Documento','Nombres','Apellidos')
    resource_class = PersonaResource


    def Nombre_Completo(self, obj):
        return obj.Nombres + " " + obj.Apellidos

    class Meta:
        	model = Personas




admin.site.register(Personas,Persona)
admin.site.register(CodigoAcceso,CodigoAccesos)
admin.site.register(TipoPersona,TipoPersonas)
