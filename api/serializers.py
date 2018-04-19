from __future__ import unicode_literals
from prestamos.models import Prestamo
from personas.models import Personas, Estudiantes, Profesores_Administrativos
from recursos.models import Tipo_Recurso, Recurso, Incidente
from configuracion.models import Programa
from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class  PersonaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Personas
       fields = ('Nro_Tarjeta', 'Id_Persona', 'Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido',
            'Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Estado_tarjeta')
       read_only_fields = ('Nro_Tarjeta', 'Id_Persona', 'Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido',
            'Tipo_Documento','Nro_Documento','Sede','genero','Correo_Institucional','Estado_tarjeta')

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ('cod','nombre')
        read_only_fields = ('cod','nombre')

class EstudiantesSerializer(serializers.ModelSerializer):
    estudiante = PersonaSerializer(many=True, read_only=True)
    programa = ProgramaSerializer(many=True, read_only=True)
    class Meta:
        model = Estudiantes
        fields = ('estudiante','Ciclo_Lectivo','programa')
        read_only_fields = ('estudiante','Ciclo_Lectivo','programa')

class Profesores_AdministrativosSerializer(serializers.ModelSerializer):
    empleado =  PersonaSerializer(many=True, read_only=True)
    class Meta:
        model = Profesores_Administrativos
        fields = ('empleado','Cargo','Dependencia')
        read_only_fields = ('empleado','Cargo','Dependencia')

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('tipo_de_recurso', 'Id_recurso', 'nombre_recurso','referencia','fecha_registro','fecha_de_baja')
        read_only_fields = ('tipo_de_recurso', 'Id_recurso', 'nombre_recurso','referencia','fecha_registro','fecha_de_baja')

class IncidenteSerializer(serializers.ModelSerializer):
    recurso =  RecursoSerializer(many=True, read_only=True)
    class Meta:
        model = Incidente
        fields = ('recurso','Fecha_Incidente','descripcion','Estado')
        read_only_fields = ('recurso','Fecha_Incidente','descripcion','Estado')

class PrestamoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=True, read_only=True)
    recurso = RecursoSerializer(many=True, read_only=True)
    class Meta:
        model = Prestamo
        fields = ('Id_prestamo', 'persona', 'recurso','Fecha_prestamo','Fecha_devolucion')
        read_only_fields = ('Id_prestamo','persona', 'recurso','Fecha_prestamo','Fecha_devolucion')
