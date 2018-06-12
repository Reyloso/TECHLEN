from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from . import views

prestamo_list = views.PrestamoList.as_view({
    'get': 'list',
    'post': 'create'
})

prestamo_detail = views.PrestamoList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

devolucion = views.PrestamoList.as_view({
    'post': 'set_devolucion'
})

urlpatterns = [
    url(r'^api/Persona/$', views.PersonasList.as_view()),
    url(r'^api/Persona/(?P<pk>\d+)/$', views.PersonasDetail.as_view()),
    url(r'^api/Prestamo/$', prestamo_list),
    url(r'^api/Prestamo/(?P<pk>\d+)/$', prestamo_detail, name='prestamo'),
    url(r'^api/Prestamo/(?P<pk>\d+)/devolucion/$', devolucion, name='devolucion_creation'),
    url(r'^api/Recurso/Incidente/$', views.IncidenteList.as_view()),
    url(r'^api/Recurso/Incidente/(?P<pk>\d+)/$', views.IncidenteDetail.as_view()),
    url(r'^api/programa/$', views.ProgramaList.as_view()),
    url(r'^api/programa/(?P<pk>\d+)/$', views.ProgramaDetail.as_view()),
    url(r'^api/recurso/$', views.RecursoList.as_view()),
    url(r'^api/recurso/(?P<pk>\d+)/$', views.RecursoDetail.as_view()),
    url(r'^api/Prestamo/Devolucion/$', views.DevolucionList.as_view()),
    url(r'^api/Prestamo/Devolucion/(?P<pk>\d+)/$', views.DevolucionDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
