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

        return "<a href='/admin/recursos/recurso/'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-plus-square' aria-hidden='true'></i>  </a>"
    Devolucion.short_description = "Devolucion"
    Devolucion.allow_tags = True
    Devolucion.is_column = True

    list_display = ['Id_prestamo','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo', 'Devolucion' ]
    search_fields = ('Id_prestamo','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo')

    class Meta:
		model = Prestamo

admin.site.register(Prestamo, Prestamos)
