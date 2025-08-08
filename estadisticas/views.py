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
    # Solo metas del usuario
    metas = MetaLectura.objects.filter(usuarios_asignados=request.user)
    total_metas = metas.count()
    # Calcular porcentaje de metas cumplidas respecto al total
    metas_cumplidas = 0
    for meta in metas:
        libros_usuario = Libro.objects.filter(usuario=request.user)
        total_libros = libros_usuario.count()
        libros_leidos = libros_usuario.filter(estado='leido').count()
        objetivo_libros = getattr(meta, 'objetivo_libros', None)
        if objetivo_libros:
            if objetivo_libros > 0 and libros_leidos >= objetivo_libros:
                metas_cumplidas += 1
        elif total_libros > 0 and libros_leidos >= total_libros:
            metas_cumplidas += 1
    if total_metas > 0:
        promedio_avance_metas = round((metas_cumplidas / total_metas) * 100, 2)
        porcentaje_metas_cumplidas = round((metas_cumplidas / total_metas) * 100, 2)
    else:
        promedio_avance_metas = 0
        porcentaje_metas_cumplidas = 0
    # Datos para gráficas
    libros_por_estado = [
        {'estado': 'Leídos', 'cantidad': libros_leidos},
        {'estado': 'Leyendo', 'cantidad': libros_leyendo},
        {'estado': 'Por leer', 'cantidad': libros_por_leer},
    ]
    notas_por_libro = list(
        libros.annotate(total_notas=models.Count('notas')).values_list('titulo', 'total_notas')
    )
    # Detalle de metas y progreso
    metas_detalle = []
    for meta in metas:
        objetivo = meta.objetivo_libros or 0
        libros_usuario = Libro.objects.filter(usuario=request.user)
        libros_leidos = libros_usuario.filter(estado='leido').count()
        avance = 0
        if objetivo > 0:
            avance = min(round((libros_leidos / objetivo) * 100, 2), 100)
        meta_info = {
            'nombre': meta.nombre,
            'tipo': meta.tipo,
            'fecha_inicio': meta.fecha_inicio,
            'fecha_fin': meta.fecha_fin,
            'objetivo_libros': objetivo,
            'avance': avance,
            'cumplida': avance >= 100,
        }
        metas_detalle.append(meta_info)
    context = {
        'total_libros': total_libros,
        'libros_leidos': libros_leidos,
        'libros_leyendo': libros_leyendo,
        'libros_por_leer': libros_por_leer,
        'total_notas': total_notas,
        'total_metas': total_metas,
        'promedio_avance_metas': promedio_avance_metas,
        'porcentaje_metas_cumplidas': porcentaje_metas_cumplidas,
        'libros_por_estado': libros_por_estado,
        'notas_por_libro': notas_por_libro,
        'metas': metas_detalle,
    }
    return render(request, 'estadisticas/index.html', context)

# Create your views here.
