from django.contrib import admin
from .models import *

# Register your models here.
class Programas (admin.ModelAdmin):
    list_display = ['cod','nombre']
    list_filter = ['nombre','cod' ]
    search_fields = ('nombre','cod')
    class Meta:
		model = Programa
class Cargos (admin.ModelAdmin):
    list_display = ['cod','Cargo']
    list_filter = ['Cargo','cod' ]
    search_fields = ('Cargo','cod')
    class Meta:
		model = Cargo
class Dependencias (admin.ModelAdmin):
    list_display = ['cod','Dependencia']
    list_filter = ['Dependencia','cod' ]
    search_fields = ('Dependencia','cod')
    class Meta:
		model = Dependencia

admin.site.register(Programa,Programas),
admin.site.register(Cargo, Cargos),
admin.site.register(Dependencia, Dependencias)
