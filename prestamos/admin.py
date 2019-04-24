# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# Register your models here.
class Prestamos (admin.ModelAdmin):
    # actions = None
    def has_add_permission(self, request):
         return False

    def get_actions(self, request):
        actions = super(Prestamos, self).get_actions(request) # Obtenemos todas las acciones de este modelo
        del actions['delete_selected'] # Deshabilitamos la opción de borrar
        return actions

    def Devolucion(self, instance):

        return "<a href='/admin/Prestamo/Detalle/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-arrow-left' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Devolucion.short_description = "Devolucion"
    Devolucion.allow_tags = True
    Devolucion.is_column = True

    def Reporte_Prestamo(self, instance):

        return "<a href='/admin/Prestamo/Reporte/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Reporte_Prestamo.short_description = "Reporte Prestamo"
    Reporte_Prestamo.allow_tags = True
    Reporte_Prestamo.is_column = True

    def add_view(self, *args, **kwargs):
        self.fields = ('Usuario_Prestatario','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion',)
        return super(Prestamos, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.fields = ('Fecha_devolucion','Estado_prestamo',)
        return super(Prestamos, self).change_view(*args, **kwargs)

    def Nombre_Completo(self, obj):
        return obj.Persona.Nombres + " " + obj.Persona.Apellidos

    list_display = ['Id_prestamo','Usuario_Prestatario','Nombre_Completo','Estado_prestamo','Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion','Reporte_Prestamo','Devolucion' ]
    search_fields = ('Id_prestamo','Usuario_Prestatario__username','Persona__Nombres','Persona__Apellidos',)
    list_filter = ('Estado_prestamo','Usuario_Prestatario__username')
    raw_id_fields = ('Persona',)

    class Meta:
        model = Prestamo

class Incidentes (admin.ModelAdmin):
    # actions = None

    def change_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(Incidentes, self).change_view(*args, **kwargs)

    # def has_add_permission(self, request):
    #     return False

    def Nombre_Completo(self, obj):
        return obj.Persona.Nombres + " " + obj.Persona.Apellidos

    # def Recurso_id(self, obj):
    #     return obj.Recurso.id

    # def Nombre_Recurso(self, obj):
    #     return obj.Recurso.Nombre_Recurso


    def Reporte_Incidente(self, instance):

        return "<a href='/admin/Incidente/Reporte/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Id_Incidente
    Reporte_Incidente.short_description = "Reporte Incidente"
    Reporte_Incidente.allow_tags = True
    Reporte_Incidente.is_column = True

    def Revision_Incidente(self, instance):

        return "<a href='/admin/Incidente/Revision/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-check-square-o' aria-hidden='true'></i>  </a>" % instance.Id_Incidente
    Revision_Incidente.short_description = "Revision Incidente"
    Revision_Incidente.allow_tags = True
    Revision_Incidente.is_column = True

    list_display = ['usuario','Nombre_Completo','Tipo_Incidente','Estado','Fecha_Incidente','Reporte_Incidente','Revision_Incidente']
    search_fields = ('Estado','Tipo_Incidente','Persona__Nombres','Persona__Apellidos','Persona__Nro_Tarjeta','usuario__username','Recurso__id')
    list_filter = ('Estado','Tipo_Incidente',)
    class Meta:
        model = Incidente

class DetallePrestamos (admin.ModelAdmin):
    #def has_add_permission(self, request):
    #    return False
        list_display = ['Id_detalle','Prestamo','Fecha_prestamo','Estado','Fecha_devolucion','Usuario_devolucion','Recurso_detalle']
        class Meta:
		          model = DetallePrestamo

class DetalleIncidentes (admin.ModelAdmin):
    #def has_add_permission(self, request):
    #    return False
        list_display = ['id','Incidente','descripcion','usuario','Fecha','Hora']
        class Meta:
		          model = DetalleIncidente


admin.site.register(DetalleIncidente, DetalleIncidentes)
admin.site.register(DetallePrestamo, DetallePrestamos)
admin.site.register(Prestamo, Prestamos)
admin.site.register(Incidente, Incidentes)
