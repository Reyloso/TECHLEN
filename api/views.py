# -*- coding: utf-8 -*-
from rest_framework import viewsets
from configuracion.models import *
from personas.models import *
from prestamos.models import *
from recursos.models import *
from rest_framework import filters
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework.decorators import action, detail_route
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework as filters
from django_filters import DateRangeFilter,DateFilter,DateTimeFromToRangeFilter


class UserViewSet(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user_request = request.user
        usuario = User.objects.get(id=user_request.id)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# vista para el tipo de persona
class TipoPersonaList(generics.ListCreateAPIView):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoPersonaSerializer

class TipoPersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoPersonaSerializer


class PersonaFilter(django_filters.FilterSet):

    class Meta:
        model = Personas
        fields = ('Nro_Tarjeta',)

#vistas de estudiantes, Profesores o adminstrativos
@action(methods=['post'], detail=True)
class PersonasList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PersonaFilter

    @detail_route(methods=['post'])
    def set_inciDetalle(self, request, pk=None):
        persona = self.get_object()
        serializer = IncidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Persona=persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer

# clase para filtro por campos
class PrestamoFilter(django_filters.FilterSet):
    Fecha_prestamo =  filters.DateTimeFilter(name='Fecha_prestamo')
    Fecha =  filters.DateTimeFromToRangeFilter(name='Fecha_prestamo')

    class Meta:
        model = Prestamo
        fields = ('Persona__Nro_Tarjeta','Fecha_prestamo','Estado_prestamo',)
        #ejemplo de consulta por los dos campos definidos
        # ?Persona=3333031643
        # ?Fecha_prestamo_0=2018-08-20&Fecha_prestamo_1=2018-08-21

#vistas del prestamo
@action(methods=['post'], detail=True)
class PrestamoList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PrestamoFilter

    @detail_route(methods=['post'])
    def set_detalleprestamo(self, request, pk=None):
        prestamo = self.get_object()
        serializer = DetallePrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Prestamo=prestamo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer


#vistas de los Incidentes
@action(methods=['post'], detail=True)
class IncidenteList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    @detail_route(methods=['post'])
    def set_detalleincidente(self, request, pk=None):
        incidente = self.get_object()
        serializer = DetalleIncidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Incidente=incidente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncidenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

#vita de detalle prestamo
class DetalleIncidenteList(generics.ListCreateAPIView):
    queryset = DetalleIncidente.objects.all()
    serializer_class = DetalleIncidenteSerializer

class DetalleIncidenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleIncidente.objects.all()
    serializer_class = DetalleIncidenteSerializer

#vistas de los programas
class ProgramaList(generics.ListCreateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class ProgramaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

#vistas de los recursos
@action(methods=['post'], detail=True)
class RecursoList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class RecursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

#vistas de el detalle_prestamo
@action(methods=['post'], detail=True)
class DetallePrestamoList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = DetallePrestamo.objects.all()
    serializer_class = DetallePrestamoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Recurso_detalle',)

    @detail_route(methods=['post'])
    def set_incidente(self, request, pk=None):
        DetallePrestamo = self.get_object()
        serializer = IncidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Prestamo_detalle=DetallePrestamo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetallePrestamo.objects.all()
    serializer_class = DetallePrestamoSerializer

class TipoRecursoList(generics.ListCreateAPIView):
    queryset = TipoRecurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

class DetalleTipoRecursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoRecurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

class MarcaList(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
