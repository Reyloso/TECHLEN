from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# Register your models here.
class Prestamos (admin.ModelAdmin):

    def Devolucion(self, instance):

        return "<a href='/admin/Prestamo/Detalle/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-chevron-circle-left' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Devolucion.short_description = "Devolucion"
    Devolucion.allow_tags = True
    Devolucion.is_column = True

    list_display = ['Id_prestamo','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo', 'Devolucion' ]
    search_fields = ('Id_prestamo','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo')

    class Meta:
		model = Prestamo

class Incidentes (admin.ModelAdmin):

        list_display = ['Id_Incidente','Fecha_Incidente','Recurso','descripcion','Estado']
        class Meta:
		          model = Incidente

admin.site.register(Prestamo, Prestamos)
admin.site.register(Incidente, Incidentes)
