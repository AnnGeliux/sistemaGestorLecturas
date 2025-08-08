
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libros.models import Libro
from metas.models import MetaLectura
from notas.models import Nota
from lectura.models import ProgresoLectura

@login_required
def dashboard(request):
    total_libros = Libro.objects.filter(usuario=request.user).count()
    total_metas = MetaLectura.objects.filter(libros_asociados__usuario=request.user).distinct().count()
    total_notas = Nota.objects.filter(libro__usuario=request.user).count()
    total_lecturas = ProgresoLectura.objects.filter(libro__usuario=request.user).count()
    return render(request, 'dashboard.html', {
        'total_libros': total_libros,
        'total_metas': total_metas,
        'total_notas': total_notas,
        'total_lecturas': total_lecturas,
    })
