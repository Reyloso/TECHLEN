from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views



urlpatterns = [
    url(r'^api/Persona/$', views.PersonasList.as_view()),
    url(r'^api/Persona/Detail/(?P<pk>\d+)/$', views.PersonasDetail.as_view()),
    url(r'^api/Prestamo/prestar/$', views.PrestamoList.as_view()),
    url(r'^api/Prestamo/Detail/(?P<pk>\d+)/$', views.PrestamoDetail.as_view(), name='prestamo'),
    url(r'^api/Recurso/Incidente/$', views.IncidenteList.as_view()),
    url(r'^api/Recurso/Incidente/(?P<pk>\d+)/$', views.IncidenteDetail.as_view()),
    url(r'^api/programa/$', views.ProgramaList.as_view()),
    url(r'^api/programa/(?P<pk>\d+)/$', views.ProgramaDetail.as_view()),
    url(r'^api/recurso/$', views.RecursoList.as_view()),
    url(r'^api/recurso/(?P<pk>\d+)/$', views.RecursoDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
