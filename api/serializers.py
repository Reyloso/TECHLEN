# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from recursos.models import Tipo_Recurso, Recurso
from personas.models import Personas
from prestamos.models import Prestamo, Incidente
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
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

    class Meta:
        model = Personas
        fields = "__all__"


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = "__all__"
