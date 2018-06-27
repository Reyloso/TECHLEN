from django.contrib import admin
from .models import *
# Register your models here.

class Recursos (admin.ModelAdmin):
        def codigo_barras(self, instance):
            return "<a href='/admin/recursos/codigo_barras/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-barcode' aria-hidden='true'></i>  </a>" % instance.Id_recurso

        codigo_barras.short_description = "Codigo De Barras"
        codigo_barras.allow_tags = True
        codigo_barras.is_column = True

        def Reporte_Recurso(self, instance):
            return "<a href='/admin/Recurso/Reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>   </a>" % instance.Id_recurso

        Reporte_Recurso.short_description = "Reporte Recurso"
        Reporte_Recurso.allow_tags = True
        Reporte_Recurso.is_column = True

        # def Incidente(self, instance):
        #     return "<a href='/admin/recursos/incidente/add/'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-check-square' aria-hidden='true'></i>  </a>"
        # Incidente.short_description = "Incidente"
        # Incidente.allow_tags = True
        # Incidente.is_column = True

        # def Devolver(self, instance):
        #     return "<a href='#'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-check-square' aria-hidden='true'></i>  </a>"
        # Devolver.short_description = "Devolver"
        # Devolver.allow_tags = True
        # Devolver.is_column = True
        list_filter = ('Estado_Recurso','tipo_de_recurso','Marca')
        search_fields = ('Id_recurso','Estado_Recurso','nombre_recurso','Numero_Serie','tipo_de_recurso__tipo_recurso','Marca__Marca','referencia')
        list_display = ['Id_recurso','Numero_Serie','tipo_de_recurso','Marca','nombre_recurso','referencia','Estado_Recurso','fecha_registro','codigo_barras','Reporte_Recurso']
        class Meta:
		          model = Recurso



admin.site.register(Tipo_Recurso)
admin.site.register(Marca)
admin.site.register(Recurso,Recursos)
