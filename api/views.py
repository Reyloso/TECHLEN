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

class UserViewSet(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user_request = request.user
        usuario = User.objects.get(id=user_request.id)
        serializer = UserSerializer(usuario)
        print serializer
        return Response(serializer.data)

#vistas de estudiantes o adminstrativos

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

    @detail_route(methods=['post'])
    def set_devolucion(self, request, pk=None):
        prestamo = self.get_object()
        serializer = DevolucionSerializer(data=request.data)
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


#vistas de las devoluciones
@action(methods=['post'], detail=True)
class DevolucionList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer

class DevolucionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializer
