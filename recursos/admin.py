from django.contrib import admin
from .models import *
# Register your models here.

class Recursos (admin.ModelAdmin):
        def codigo_barras(self, instance):
            return "<a href='/admin/recursos/codigo_barras/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-barcode' aria-hidden='true'></i>  </a>" % instance.Id_recurso

        codigo_barras.short_description = "Codigo De Barras"
        codigo_barras.allow_tags = True
        codigo_barras.is_column = True
        list_display = ['Id_recurso','tipo_de_recurso','nombre_recurso','referencia','Estado_Recurso','fecha_registro','codigo_barras']
        class Meta:
		          model = Recurso

admin.site.register(Tipo_Recurso)
admin.site.register(Recurso,Recursos)
admin.site.register(Incidente)
