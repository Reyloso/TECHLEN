# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from recursos.models import Recurso
from django.contrib import admin
from prestamos.models import Prestamo, Incidente
from personas.models import Personas
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')


@login_required(redirect_field_name='core/prestamo.html')
def prestamo_prestar(request):
    context = admin.site.each_context(request)
    context.update({
        'title': 'Prestar',
    })
    return render(request, 'core/prestamo.html', context)

@login_required
def codigo_barras(request,Id_recurso):
    r = get_object_or_404(Recurso,Id_recurso=Id_recurso)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/codigo_barras.html',context)

@login_required
def detalle_prestamo(request,Id_prestamo):
    r = get_object_or_404(Prestamo,Id_prestamo=Id_prestamo)
    context = admin.site.each_context(request)
    context.update({
        'title': 'Detalle Prestamo',
        'r': r,
    })
    return  render(request,'core/detalle_prestamo.html',context)

@login_required
def persona_reporte(request,Nro_Tarjeta):
    r = get_object_or_404(Personas,Nro_Tarjeta=Nro_Tarjeta)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/reporte_persona.html',context)

@login_required
def prestamo_reporte(request,Id_prestamo):
    r = get_object_or_404(Prestamo,Id_prestamo=Id_prestamo)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/reporte_prestamo.html',context)

@login_required
def recurso_reporte(request,Id_recurso):
    r = get_object_or_404(Recurso,Id_recurso=Id_recurso)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/reporte_recurso.html',context)

@login_required
def incidente_reporte(request,Id_Incidente):
    r = get_object_or_404(Incidente,Id_Incidente=Id_Incidente)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/Reporte_Incidente.html',context)

@login_required
def incidente_revision(request,Id_Incidente):
    r = get_object_or_404(Incidente,Id_Incidente=Id_Incidente)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/revision_Incidente.html',context)

@login_required
def reporte(request):
    context = admin.site.each_context(request)
    return  render(request,'core/Reporte.html',context)

@login_required
def handler404(request):
    return render(request, 'admin/404.html', status=404)

@login_required
def handler500(request):
    return render(request, 'admin/500.html', status=500)
