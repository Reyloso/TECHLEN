from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views



urlpatterns = [
    url(r'^api/Estudiante/$', views.EstudiantesList.as_view()),
    url(r'^api/Estudiante/(?P<Id_Persona>\d+)/$', views.EstudiantesDetail.as_view()),
    url(r'^api/Prestamo/prestar/$', views.PrestamoList),
    url(r'^api/Prestamo/prestar/(?P<Nro_Tarjeta>\d+)/$', views.PrestamoDetail.as_view()),
    url(r'^api/Recurso/Registro_Incidente$', views.IncidenteList),
    url(r'^api/Recurso/Registro_Incidente/(?P<Id_Incidente>\d+)/$', views.IncidenteDetail),
    url(r'^api/programa/$', views.ProgramaList.as_view()),
    url(r'^api/programa/(?P<Id_Persona>\d+)/$', views.ProgramaDetail.as_view()),
    url(r'^api/recurso/$', views.RecursoList.as_view()),
    url(r'^api/recurso/(?P<Id_Persona>\d+)/$', views.RecursoDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
