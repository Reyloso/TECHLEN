from django.contrib import admin
from .models import *
# Register your models here.

class Recursos (admin.ModelAdmin):
    actions = None

    def change_view(self, *args, **kwargs):
        self.fields = ('nombre_recurso','referencia','Estado_Recurso')
        return super(Recursos, self).change_view(*args, **kwargs)

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

    list_filter = ('Estado_Recurso','tipo_de_recurso','Marca')
    search_fields = ('Id_recurso','Estado_Recurso','nombre_recurso','Numero_Serie','tipo_de_recurso__tipo_recurso','Marca__Marca','referencia')
    list_display = ['Id_recurso','Numero_Serie','tipo_de_recurso','Marca','nombre_recurso','referencia','Estado_Recurso','fecha_registro','codigo_barras','Reporte_Recurso']
    class Meta:
        model = Recurso


class  Marcas (admin.ModelAdmin):
    actions = None

    class Meta:
        model = Marca

class  Tipo_Recursos (admin.ModelAdmin):
    actions = None

    class Meta:
        model = Tipo_Recurso

admin.site.register(Tipo_Recurso,Tipo_Recursos)
admin.site.register(Marca,Marcas)
admin.site.register(Recurso,Recursos)
