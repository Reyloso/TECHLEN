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

#vistas de estudiantes, Profesores o adminstrativos
@action(methods=['post'], detail=True)
class PersonasList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer

    @detail_route(methods=['post'])
    def set_incidente(self, request, pk=None):
        persona = self.get_object()
        serializer = IncidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Persona=persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer

#vistas del prestamo
@action(methods=['post'], detail=True)
class PrestamoList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Estado_prestamo','Persona','Fecha_prestamo','Fecha_devolucion',)

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
class IncidenteList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

class IncidenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

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
    queryset = Tipo_Recurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

class DetallePrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipo_Recurso.objects.all()
    serializer_class = Tipo_RecursoSerializer

class MarcaList(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
