from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class RecursosResource(resources.ModelResource):
    tipo_de_recurso = fields.Field(attribute='tipo_de_recurso',
                                   widget=ForeignKeyWidget(TipoRecurso, 'tipo_recurso'))

    Marca = fields.Field(attribute='Marca',
                                   widget=ForeignKeyWidget(Marca, 'Marca'))
    class Meta:
        # import_id_fields = ('id',)
        model = Recurso
        export_order = ('id','nombre_recurso','tipo_de_recurso','Marca','Numero_Serie','referencia','Estado_Recurso')
        fields =  ('id','nombre_recurso','tipo_de_recurso','Marca','Numero_Serie','referencia','Estado_Recurso')

class Recursos (ImportExportModelAdmin):
    actions = None

    def codigo_barras(self, instance):
        return "<a href='/admin/recursos/codigo_barras/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-barcode' aria-hidden='true'></i>  </a>" % instance.id

    codigo_barras.short_description = "Codigo De Barras"
    codigo_barras.allow_tags = True
    codigo_barras.is_column = True

    def Reporte_Recurso(self, instance):
        return "<a href='/admin/Recurso/Reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>   </a>" % instance.id

    Reporte_Recurso.short_description = "Reporte Recurso"
    Reporte_Recurso.allow_tags = True
    Reporte_Recurso.is_column = True

    list_filter = ('Estado_Recurso','tipo_de_recurso','Marca')
    search_fields = ('Estado_Recurso','nombre_recurso','Numero_Serie','tipo_de_recurso__tipo_recurso','Marca__Marca','referencia')
    list_display = ['id','Numero_Serie','tipo_de_recurso','Marca','nombre_recurso','referencia','Estado_Recurso','fecha_registro','codigo_barras','Reporte_Recurso']
    resource_class = RecursosResource
    class Meta:
        model = Recurso


class  Marcas (admin.ModelAdmin):
    actions = None

    class Meta:
        model = Marca

class  Tipo_Recursos (admin.ModelAdmin):
    actions = None

    class Meta:
        model = TipoRecurso

admin.site.register(TipoRecurso,Tipo_Recursos)
admin.site.register(Marca,Marcas)
admin.site.register(Recurso,Recursos)
