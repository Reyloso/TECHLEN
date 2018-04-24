# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from recursos.models import Tipo_Recurso, Recurso, Incidente
from personas.models import Personas, Estudiantes, Profesores_Administrativos
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

class Tipo_RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Recurso
        fields = ('id_recurso', 'tipo_recurso')

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('Id_recurso', 'tipo_de_recurso', 'nombre_recurso','referencia',
        'fecha_registro','fecha_de_baja')

class IncidenteSerializer(serializers.ModelSerializer):
    recurso = RecursoSerializer(many=True, read_only=True)

    class Meta:
        model = Incidente
        fields = ('Id_Incidente', 'Fecha_Incidente', 'descripcion','Estado',
        'recurso')

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personas
        fields = ('Nro_Tarjeta', 'Id_Persona', 'Primer_Nombre','Segundo_Nombre',
        'Primer_Apellido', 'Segundo_Apellido', 'Tipo_Documento', 'Nro_Documento',
        'Sede', 'genero', 'Correo_Institucional', 'Estado_tarjeta')

class EstudiantesSerializer(PersonaSerializer):
    programa = ProgramaSerializer(many=True, read_only=True)

    class Meta:
        model = Estudiantes
        fields =  "__all__"

class Profesores_AdministrativosSerializer(PersonaSerializer):

    class Meta:
        model = Profesores_Administrativos
        fields = "__all__"

class PrestamoSerializer(serializers.ModelSerializer):
    persona = EstudiantesSerializer(many=True, read_only=True)
    recurso = RecursoSerializer(many=True, read_only=True)

    class Meta:
        model = Prestamo
        fields = "__all__"
