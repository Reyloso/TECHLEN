from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# Register your models here.
class Prestamos (admin.ModelAdmin):
    # def has_add_permission(self, request):
    #     return False

    def Devolucion(self, instance):

        return "<a href='/admin/Prestamo/Detalle/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-chevron-circle-left' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Devolucion.short_description = "Devolucion"
    Devolucion.allow_tags = True
    Devolucion.is_column = True

    def add_view(self, *args, **kwargs):
        self.fields = ('Usuario_Prestatario','Persona','recurso','Estado_prestamo','Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion',)
        return super(Prestamos, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.fields = ('recurso','Estado_prestamo',)
        return super(Prestamos, self).change_view(*args, **kwargs)

    list_display = ['Id_prestamo','Usuario_Prestatario','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo', 'Devolucion' ]
    search_fields = ('Id_prestamo','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo')
    list_filter = ('Estado_prestamo','Usuario_Prestatario__username')

    class Meta:
		model = Prestamo

class Incidentes (admin.ModelAdmin):
    # def has_add_permission(self, request):
    #     return False

        list_display = ['Id_Incidente','Fecha_Incidente','Recurso','descripcion','Estado']
        list_filter = ('Estado',)
        class Meta:
		          model = Incidente

class Devoluciones (admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

        list_display = ['Id_devolucion','Prestamo','Usuario_devolucion','Recurso_devolucion','Fecha_devolucion']
        class Meta:
		          model = Devolucion



admin.site.register(Devolucion, Devoluciones)
admin.site.register(Prestamo, Prestamos)
admin.site.register(Incidente, Incidentes)
