from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from . import views

#vista personalizada prestamo
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

Detalle_prestamo = views.PrestamoList.as_view({
    'post': 'set_detalleprestamo'
})

#vista personalizada persona
persona_list = views.PersonasList.as_view({
    'get': 'list',
    'post': 'create'
})

persona_detail = views.PersonasList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

incidente = views.PersonasList.as_view({
    'post': 'set_incidente'
})

#vista personalizada detalle pretsamo
detallep_list = views.DetallePrestamoList.as_view({
    'get': 'list',
    'post': 'create'
})

detallep_detail = views.DetallePrestamoList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

incidentep = views.DetallePrestamoList.as_view({
    'post': 'set_incidente'
})

urlpatterns = [
    url(r'^api/Persona/$', persona_list),
    url(r'^api/Persona/(?P<pk>\d+)/$', persona_detail),
    url(r'^api/Persona/(?P<pk>\d+)/incidentes/$', incidente),
    url(r'^api/Persona/tipo/$', views.TipoPersonaList.as_view()),
    url(r'^api/Persona/tipo/(?P<pk>\d+)/$', views.TipoPersonaDetail.as_view()),
    url(r'^api/Prestamo/$', prestamo_list),
    url(r'^api/Prestamo/(?P<pk>\d+)/$', prestamo_detail),
    url(r'^api/Prestamo/(?P<pk>\d+)/devolucion/$', Detalle_prestamo),
    url(r'^api/Recurso/Incidente/$', views.IncidenteList.as_view()),
    url(r'^api/Recurso/Incidente/(?P<pk>\d+)/$', views.IncidenteDetail.as_view()),
    url(r'^api/Recurso/Tipo/$', views.TipoRecursoList.as_view()),
    url(r'^api/Recurso/Marca/$', views.MarcaList.as_view()),
    url(r'^api/programa/$', views.ProgramaList.as_view()),
    url(r'^api/programa/(?P<pk>\d+)/$', views.ProgramaDetail.as_view()),
    url(r'^api/recurso/$', views.RecursoList.as_view()),
    url(r'^api/recurso/(?P<pk>\d+)/$',views.RecursoDetail.as_view()),
    url(r'^api/Prestamo/Detalle/$', detallep_list),
    url(r'^api/Prestamo/Detalle/(?P<pk>\d+)/$', detallep_detail),
    url(r'^api/Prestamo/Detalle/(?P<pk>\d+)/incidentes/$', incidentep),
    url(r'^api/User/$', views.UserViewSet.as_view()),
    url(r'^api/User/(?P<pk>\d+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
