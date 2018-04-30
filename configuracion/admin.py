from django.contrib import admin
from .models import *

# Register your models here.
class Programas (admin.ModelAdmin):
    list_display = ['cod','nombre']
    list_filter = ['nombre','cod' ]
    search_fields = ('nombre','cod')
    class Meta:
		model = Programa


admin.site.register(Programa,Programas)
