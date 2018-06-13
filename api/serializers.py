# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from recursos.models import Tipo_Recurso, Recurso
from personas.models import Personas
from prestamos.models import Prestamo, Incidente, Devolucion
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','get_full_name', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = "__all__"

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = "__all__"

class Tipo_RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = "__all__"

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):
    Programa_Academico = ProgramaSerializer(read_only=True)
    ProgramaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Programa_Academico')
    Incidentes = IncidenteSerializer(many=True, read_only=True, source='incidente_set')

    class Meta:
        model = Personas
        fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Estado_tarjeta','Tipo_Persona','Programa_Academico','ProgramaId','Ciclo_Lectivo','Incidentes')


class DevolucionSerializer(serializers.ModelSerializer):
    Usuario_devolucion = UserSerializer(read_only=True)
    UsuarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Usuario_devolucion')
    class Meta:
        model = Devolucion
        fields = ('Id_devolucion','Prestamo','Fecha_devolucion','Usuario_devolucion','UsuarioId','Recurso_devolucion')

class PrestamoSerializer(serializers.ModelSerializer):
    Usuario_Prestatario = UserSerializer(read_only=True)
    PrestatarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Usuario_Prestatario')
    Persona = PersonaSerializer(read_only=True)
    personaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Personas.objects.all(), source='Persona')
    devoluciones = DevolucionSerializer(many=True, read_only=True, source='devolucion_set')

    class Meta:
        model = Prestamo
        fields = ('Id_prestamo', 'Usuario_Prestatario','PrestatarioId', 'Persona', 'personaId','recurso', 'Estado_prestamo', 'Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion','devoluciones')
