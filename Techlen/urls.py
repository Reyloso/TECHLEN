"""TECHLEN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from api import views
from core import views
from core.views import handler404, handler404

handler404 = handler404
handler500 = handler404
urlpatterns = [
    #url(r'^$', include('core.urls')),

    url(r'^$',  views.inicio, name='inicio'),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/Prestamo/Prestar/',  views.prestamo_prestar, name='prestamo-prestar'),
    url(r'^admin/recursos/codigo_barras/(?P<Id_recurso>[\w\-]+)$', views.codigo_barras, name='codigo-barras'),
    url(r'^admin/Prestamo/Detalle/(?P<Id_prestamo>[\w\-]+)$', views.detalle_prestamo, name='detalle-prestamo'),
    url(r'^admin/persona/Reporte/(?P<Nro_Tarjeta>[\w\-]+)$',  views.persona_reporte, name='Persona-Reporte'),
    url(r'^admin/Recurso/Reporte/(?P<Id_recurso>[\w\-]+)$',  views.recurso_reporte, name='Recurso-Reporte'),
    url(r'^admin/Prestamo/Reporte/(?P<Id_prestamo>[\w\-]+)$',  views.prestamo_reporte, name='Prestamo-Reporte'),
    url(r'^admin/Incidente/Reporte/(?P<Id_Incidente>[\w\-]+)$',  views.incidente_reporte, name='Incidente-Reporte'),
    url(r'^admin/Reporte/',  views.reporte, name='Reporte'),
    url(r'', include('api.urls')),

]
