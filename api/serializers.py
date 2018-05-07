# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from recursos.models import Tipo_Recurso, Recurso, Incidente
from personas.models import Personas
from prestamos.models import Prestamo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ('cod', 'nombre')

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = ('Id_Incidente', 'Fecha_Incidente', 'descripcion','Estado')

class Tipo_RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = ('id_recurso', 'tipo_recurso')

class RecursoSerializer(serializers.ModelSerializer):
    Incidentes = IncidenteSerializer(many=True, read_only=True)
    class Meta:
        model = Recurso
        fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personas
        fields = "__all__"


class PrestamoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=True, read_only=True)
    recurso = RecursoSerializer(many=True, read_only=True)
    class Meta:
        model = Prestamo
        fields = "__all__"
