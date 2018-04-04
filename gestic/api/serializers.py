# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prestamos.models import Prestamo, Incidencia, Detalle_Prestamo
from personas.models import Personas, Tipo_persona, Estudiantes, Profesores_Administrativos
from recursos.models import Tipo_Recurso, Recurso, Registro_Incidente
from configuracion.models import Programa
from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class  PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Personas
       fields = ('Nro_Tarjeta', 'Id_Persona', 'Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido',
            'Tipo_Documento','Nro_Documento','Sede','Codigo_ops','genero','Correo_Institucional','Formato_credencial','Grupo_acceso','Estado_tarjeta','foto_url')
       read_only_fields = ('Nro_Tarjeta', 'Id_Persona', 'Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido',
            'Tipo_Documento','Nro_Documento','Sede','Codigo_ops','genero','Correo_Institucional','Formato_credencial','Grupo_acceso','Estado_tarjeta','foto_url')

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('cod','nombre')
        read_only_fields = ('cod','nombre')

class EstudiantesSerializer(serializers.Serializer):
    estudiante = PersonaSerializer(read_only=True)
    programa = ProgramaSerializer(read_only=True)
    class Meta:
        model = Estudiantes
        fields = ('estudiante','programa','Ciclo_Lectivo','Programa_Academico')
        read_only_fields = ('estudiante','programa','Ciclo_Lectivo','Programa_Academico')

class Profesores_AdministrativosSerializer(serializers.HyperlinkedModelSerializer):
    empleado =  PersonaSerializer(read_only=True)
class Meta:
    model = Profesores_Administrativos
    fields = ('empleado','Cargo','Dependencia')
    read_only_fields = ('empleado','Cargo','Dependencia')

class IncidenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidencia
        fields = ('Fecha_Incidencia')
        read_only_fields = ('Fecha_Incidencia')

class RecursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recurso
        fields = ('tipo_de_recurso', 'Id_recurso', 'nombre_recurso','referencia','fecha_registro','fecha_de_baja')
        read_only_fields = ('tipo_de_recurso', 'Id_recurso', 'nombre_recurso','referencia','fecha_registro','fecha_de_baja')

class Registro_IncidenteSerializer(serializers.HyperlinkedModelSerializer):
    recurso =  RecursoSerializer(read_only=True)
    class Meta:
        model = Registro_Incidente
        fields = ('recurso','Fecha_Incidente','descripcion','Estado')
        read_only_fields = ('recurso','Fecha_Incidente','descripcion','Estado')

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    persona = PersonaSerializer(read_only=True)
    class Meta:
        model = Prestamo
        fields = ('id_prestamo', 'persona', 'Fecha_prestamo','Fecha_devolucion')
        read_only_fields = ('id_prestamo', 'persona', 'Fecha_prestamo','Fecha_devolucion')

class Detalle_PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    incidente = IncidenciaSerializer(read_only=True)
    prestamo = PrestamoSerializer(read_only=True)
    recurso = RecursoSerializer(read_only=True)
    class Meta:
        model = Detalle_Prestamo
        fields = ('incidente', 'prestamo', 'recurso')
        read_only_fields = ('incidente', 'prestamo', 'recurso')
