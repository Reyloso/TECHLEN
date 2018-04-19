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


class Profesores_AdministrativosView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):


    queryset = Profesores_Administrativos.objects.all()
    serializer_class = Profesores_AdministrativosSerializer

    def list(self, request, *args, **kwargs):
        queryset = Profesores_Administrativos.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        custom_data = {'pograma_results': {'pograma_array': serializer_data}}
        return Response(custom_data)

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)



class PrestamoView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('Id_prestamo',)
    http_method_names = ('post', 'get')

    @api_view(['GET', 'POST'])
    def get_prestamo(request, Nro_Tarjeta ):
        id_e = request.GET.get("id")
        id_r = request.GET.get("id")
        print(id_e)
        serializer_p = PersonaSerializer(Personas.objects.get(Nro_Tarjeta=id_e))
        serializer_r = RecursoSerializer(Recurso.objects.get(Id_recurso=id_r))
        r = {
            "persona": serialized_p.data.pop('Personas'),
            "recursos": serializer_r.data.pop('Recurso'),
        }

        rp = self.list(r)
        return rp

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        custom_data = {'pograma_results': {'pograma_array': serializer_data}}
        return Response(custom_data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProgramaView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^=cod', '^=nombre')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        custom_data = {'pograma_results': {'pograma_array': serializer_data}}
        return Response(custom_data)

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

class IncidenteView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
