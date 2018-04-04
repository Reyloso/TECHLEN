# -*- coding: utf-8 -*-
from rest_framework import viewsets

from configuracion.models import *
from personas.models import *
from prestamos.models import *
from recursos.models import *
from rest_framework import filters
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request

class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)

class LogoutViewCustom(LogoutView):
    authentication_classes = (TokenAuthentication,)

class UsuarioViewSet(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user_request = request.user
        usuario = User.objects.get(id=user_request.id)
        serializer = UsuarioSerializer(usuario)
        print serializer
        return Response(serializer.data)

class EstudiantesView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)

class Profesores_AdministrativosView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):


    queryset = Profesores_Administrativos.objects.all()
    serializer_class = Profesores_AdministrativosSerializer

class PrestamoView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IncidenciaView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer

class ProgramaView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RecursoView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Registro_IncidenteView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Registro_Incidente.objects.all()
    serializer_class = Registro_IncidenteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Detalle_PrestamoView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Detalle_Prestamo.objects.all()
    serializer_class = Detalle_PrestamoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
