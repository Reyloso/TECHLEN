from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html', {})


@login_required(redirect_field_name='core/prestamo.html')
def prestamsrfid(request):


    return render(request, 'core/prestamo.html', {})
