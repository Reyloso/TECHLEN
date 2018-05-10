from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from recursos.models import Recurso
from django.contrib import admin


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html', {})


@login_required(redirect_field_name='core/prestamo.html')
def prestamo_prestar(request):
    context = admin.site.each_context(request)
    return render(request, 'core/prestamo.html', context)

@login_required
def codigo_barras(request,Id_recurso):
    r = get_object_or_404(Recurso,Id_recurso=Id_recurso)
    context = admin.site.each_context(request)
    context.update({
        'r': r,
    })
    return  render(request,'core/codigo_barras.html',context)
