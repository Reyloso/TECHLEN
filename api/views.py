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
    filter_fields = ('id_prestamo',)
    http_method_names = ('post', 'get')

    def get(self, request):
        id_e = request.GET.get("id")
        id_r = request.GET.get("id")
        print(id_e)

        serializer_p = Personas.objects.get(Nro_Tarjeta=id_e)
        serializer_r = Personas.objects.get(Id_recurso=id_r)
        custom_data_p = {'prestamo_results': {'prestamo_array': "hola"}}
        custom_data_r = {'recurso_results': {'recurso_array': serializer_r.data}}


        return render_to_response(Request, 'add_prestamo.html', custom_data_p )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IncidenciaView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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
