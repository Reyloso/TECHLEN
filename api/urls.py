from django.conf.urls import include, url
from django.contrib import admin
from .routers import DefaultRouterWithSimpleViews
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouterWithSimpleViews()
router.register(r'login', LoginViewCustom, base_name='login')
router.register(r'logout', LogoutViewCustom, base_name='logout')
router.register(r'usuario', UsuarioViewSet, base_name='usuario')
router.register(r'Estudiante', EstudiantesView, base_name='Estudiante')
router.register(r'Empleado', Profesores_AdministrativosView, base_name='Empleado')
router.register(r'Prestamo/persona', PrestamoView, base_name='Prestar')
router.register(r'Programa', ProgramaView, base_name='Programa')
router.register(r'Recurso', RecursoView, base_name='Recurso')
router.register(r'Recurso/Registro_Incidente', IncidenteView, base_name='Registro_Incidente')

urlpatterns = [
    url(r'api/', include(router.urls, namespace='api')),
    url(r'^api/auth/', include('rest_framework.urls')),
    url(r'^api/Estudiante/$', EstudiantesView),
    url(r'^api/Empleado/$',Profesores_AdministrativosView),
    url(r'^api/Prestamo/$',PrestamoView),
    url(r'^api/Prestamo/prestar/(?P<Nro_Tarjeta>\d+)/$', PrestamoView.as_view()),
    url(r'^api/Recurso/Registro_Incidente$', IncidenteView),
    url(r'^api/Recurso/$', RecursoView.as_view()),
    url(r'^api/Recurso/(?P<Id_recurso>\d+)/$', RecursoView),
    url(r'^api/Recurso/Registro_Incidente/(?P<id>\d+)/$', IncidenteView),

]
