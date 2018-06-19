# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from recursos.models import Tipo_Recurso, Recurso
from personas.models import Personas
from prestamos.models import Prestamo, Incidente, DetallePrestamo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','get_full_name', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class Tipo_RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = "__all__"

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = "__all__"
        #fields = ('Id_recurso','tipo_de_recurso','Marca','nombre_recurso','referencia','Estado_Recurso','fecha_registro','Detalle_Prestamo')

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = "__all__"

class DetallePrestamoSerializer(serializers.ModelSerializer):
    Recurso_detalle = RecursoSerializer(read_only=True)
    recursoid = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Recurso.objects.all(), source='Recurso_detalle')
    class Meta:
        model = DetallePrestamo
        fields = fields = ('Id_detalle','Fecha_prestamo', 'Estado','Fecha_devolucion','Prestamo','Usuario_devolucion','recursoid','Recurso_detalle')

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):
    Programa_Academico = ProgramaSerializer(read_only=True)
    ProgramaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Programa.objects.all(), source='Programa_Academico')
    Incidentes = IncidenteSerializer(many=True, read_only=True,source='incidente_set')

    class Meta:
        model = Personas
        fields = ('Nro_Tarjeta','Id_Persona','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Estado_tarjeta','Tipo_Persona','Programa_Academico','ProgramaId','Ciclo_Lectivo','Incidentes')


class PrestamoSerializer(serializers.ModelSerializer):
    Usuario_Prestatario = UserSerializer(read_only=True)
    PrestatarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Usuario_Prestatario')
    Persona = PersonaSerializer(read_only=True)
    personaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Personas.objects.all(), source='Persona')
    detalleprestamo = DetallePrestamoSerializer(many=True,write_only=True)
    detailprestamo = DetallePrestamoSerializer(many=True,read_only=True,source='detalleprestamo_set')

    class Meta:
        model = Prestamo
        fields = ('Id_prestamo', 'Usuario_Prestatario','PrestatarioId', 'Persona', 'personaId', 'Estado_prestamo', 'Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion','detalleprestamo','detailprestamo')

    def create(self, validated_data):
        detalleprestamo_data = validated_data.pop('detalleprestamo')
        prestamo = Prestamo.objects.create(**validated_data)
        print detalleprestamo_data
        for Detalle_data in detalleprestamo_data:
            DetallePrestamo.objects.create(Prestamo=prestamo,**Detalle_data)
        return prestamo
