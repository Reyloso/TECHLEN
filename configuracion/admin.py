# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
class ProgramasResource(resources.ModelResource):
    actions = None
    class Meta:
        import_id_fields = ('cod',)
        model = Programa
        export_order = ('nombre','cod')
        fields =  ('cod','nombre')

class Programas (ImportExportModelAdmin):
    actions = None
    list_display = ['cod','nombre']
    list_filter = ['nombre']
    search_fields = ('nombre','cod')
    resource_class = ProgramasResource
    class Meta:
        model = Programa

admin.site.register(Programa,Programas),
