
from django.shortcuts import render
from libros.models import Libro
from notas.models import Nota
from metas.models import MetaLectura

from django.contrib.auth.decorators import login_required
from django.db import models

@login_required
def index(request):
    libros = Libro.objects.filter(usuario=request.user)
    total_libros = libros.count()
    libros_leidos = libros.filter(estado='leido').count()
    libros_leyendo = libros.filter(estado='leyendo').count()
    libros_por_leer = libros.filter(estado='por_leer').count()
    total_notas = Nota.objects.filter(libro__usuario=request.user).count()
    total_metas = MetaLectura.objects.count()
    metas = MetaLectura.objects.all()
    if metas.exists():
        promedio_avance_metas = round(sum([float(m.porcentaje_avance) for m in metas]) / metas.count(), 2)
    else:
        promedio_avance_metas = 0
    # Datos para gráficas
    libros_por_estado = [
        {'estado': 'Leídos', 'cantidad': libros_leidos},
        {'estado': 'Leyendo', 'cantidad': libros_leyendo},
        {'estado': 'Por leer', 'cantidad': libros_por_leer},
    ]
    notas_por_libro = list(
        libros.annotate(total_notas=models.Count('notas')).values_list('titulo', 'total_notas')
    )
    context = {
        'total_libros': total_libros,
        'libros_leidos': libros_leidos,
        'libros_leyendo': libros_leyendo,
        'libros_por_leer': libros_por_leer,
        'total_notas': total_notas,
        'total_metas': total_metas,
        'promedio_avance_metas': promedio_avance_metas,
        'libros_por_estado': libros_por_estado,
        'notas_por_libro': notas_por_libro,
    }
    return render(request, 'estadisticas/index.html', context)

# Create your views here.
