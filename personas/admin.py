# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from configuracion.models import *
from django.contrib.auth.admin import GroupAdmin, UserAdmin 
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission

# Register your models here.

class CodigoAccesos (admin.ModelAdmin):
        actions = None
        list_display = ['id','Codigo']
        class Meta:
		          model = CodigoAcceso

class TipoPersonas (admin.ModelAdmin):
        actions = None
        list_display = ['id','Tipo_persona']
        class Meta:
		          model = TipoPersona


class PersonaResource(resources.ModelResource):

	Dependencia = fields.Field(attribute='Dependencia',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	Tipo_Persona = fields.Field(attribute='Tipo_Persona',
								   widget=ForeignKeyWidget(TipoPersona, 'Tipo_persona'))

	Codigo_Acceso = fields.Field(attribute='Codigo_Acceso',
								   widget=ForeignKeyWidget(CodigoAcceso, 'Codigo'))


	class Meta:
		import_id_fields = ('Nro_Tarjeta',)
		model = Personas
		export_order = ('Apellidos','Nombres','Dependencia','Nro_Tarjeta','Tipo_Persona','Codigo_Acceso','Estado_Tarjeta','Nro_Documento')
		fields =  ('Nro_Tarjeta','Nro_Documento','Nombres','Apellidos','Estado_Tarjeta','Tipo_Persona','Dependencia','Codigo_Acceso')

class Persona (ImportExportModelAdmin):
    list_per_page = 40
    # actions = None
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def change_view(self, *args, **kwargs):
        self.fields = ('Nro_Tarjeta','Nro_Documento','Nombres','Apellidos','Estado_Tarjeta','Tipo_Persona','Dependencia','Codigo_Acceso')
        return super(Persona, self).change_view(*args, **kwargs)

    def reporte_prestamos(self, instance):
        return "<a href='/admin/persona/Reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Nro_Tarjeta

    reporte_prestamos.short_description = "Reporte Persona"
    reporte_prestamos.allow_tags = True
    reporte_prestamos.is_column = True

    list_display = ['id','Nro_Tarjeta','Nro_Documento','Nombre_Completo','Estado_Tarjeta','Tipo_Persona','Dependencia','Codigo_Acceso','reporte_prestamos']
    list_filter = ['Dependencia','Estado_Tarjeta','Tipo_Persona','Codigo_Acceso']
    search_fields = ('Nro_Tarjeta','Nro_Documento','Nombres','Apellidos')
    resource_class = PersonaResource

    def Nombre_Completo(self, obj):
        return obj.Nombres + " " + obj.Apellidos

    class Meta:
        	model = Personas



# admin usuario 

class PermissionFilterMixin(object):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ('permissions', 'user_permissions'):
            qs = kwargs.get('queryset', db_field.rel.to.objects)
            qs = _filter_permissions(qs)
            kwargs['queryset'] = qs
           

        return super(PermissionFilterMixin, self).formfield_for_manytomany(db_field, request, **kwargs)

class MyGroupAdmin(PermissionFilterMixin, GroupAdmin):
    pass

class UserAdmins(PermissionFilterMixin, UserAdmin):
    # list_display = ('username','first_name','last_name','email','is_staff','is_superuser','last_login','date_joined')
    def get_queryset(self, request):
        qs = super(UserAdmins, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else :
            return qs.filter(username=request.user)

    def get_fieldsets(self, request, obj=None):
        if obj:
            if request.user.is_superuser :
                return (
                    (None, {'fields': ('username', 'password')}),
                    (('Información Personal'), {'fields': ('first_name', 'last_name', 'email')}),
                    (('Permisos'), {'fields': ('is_superuser','is_active', 'is_staff', 'user_permissions')}),
                    (('Fechas Importantes'), {'fields': ('last_login', 'date_joined')}),
                )
            else:
                return (
                    (None, {'fields': ('password')}),
                    (('Información Personal'), {'fields': ('first_name', 'last_name', 'email')}),
                )
        else:
            return self.add_fieldsets
        
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User,UserAdmins)
admin.site.register(Group, MyGroupAdmin)
admin.site.register(Personas,Persona)
admin.site.register(CodigoAcceso,CodigoAccesos)
admin.site.register(TipoPersona,TipoPersonas)


def _filter_permissions(qs):
    return qs.exclude(codename__in=(
        # Has no admin interface:
        'add_permission',
        'change_permission',
        'delete_permission',

        'add_contenttype',
        'change_contenttype',
        'delete_contenttype',

        'add_session',
        'delete_session',
        'change_session',

        # django.contrib.admin
        'add_logentry',
        'change_logentry',
        'delete_logentry',


        # sorl-thumbnail    
        'add_kvstore',
        'change_kvstore',
        'delete_kvstore',

        # south
        'add_migrationhistory',
        'change_migrationhistory',
        'delete_migrationhistory',

        # django-admin-tools    
        'add_dashboardpreferences',
        'change_dashboardpreferences',
        'delete_dashboardpreferences',

    )) \
    .exclude(codename__endswith='userobjectpermission') \
    .exclude(codename__endswith='groupobjectpermission')  

