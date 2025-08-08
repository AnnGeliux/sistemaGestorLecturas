from django.shortcuts import render, redirect
from .models import MetaLectura
from .forms import MetaLecturaForm
from libros.models import Libro
from notas.models import Nota
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def index(request):
    if request.user.is_superuser or request.user.is_staff:
        metas = MetaLectura.objects.all()
    else:
        metas = MetaLectura.objects.filter(usuarios_asignados=request.user)
    progreso = []
    for meta in metas:
        # Determinar el usuario principal de la meta (el primero asignado, o el creador si no hay asignados)
        usuarios_meta = meta.usuarios_asignados.all()
        if usuarios_meta.exists():
            usuario_meta = usuarios_meta.first()
        else:
            usuario_meta = meta.creador
        libros_usuario = Libro.objects.filter(usuario=usuario_meta)
        total_libros = libros_usuario.count()
        libros_leidos = libros_usuario.filter(estado='leido').count()
        objetivo_libros = getattr(meta, 'objetivo_libros', None)
        objetivo_notas = getattr(meta, 'objetivo_notas', None)
        notas_por_libro = {}
        if objetivo_notas:
            for libro in libros_usuario:
                notas = Nota.objects.filter(libro=libro).count()
                notas_por_libro[libro.titulo] = notas
        # Calcular porcentaje de cumplimiento
        if objetivo_libros:
            if objetivo_libros > 0:
                porcentaje = min(100, int((libros_leidos / objetivo_libros) * 100))
            else:
                porcentaje = 0
        else:
            porcentaje = int((libros_leidos / total_libros) * 100) if total_libros > 0 else 0
        progreso.append({
            'meta': meta,
            'total_libros': total_libros,
            'libros_leidos': libros_leidos,
            'objetivo_libros': objetivo_libros,
            'objetivo_notas': objetivo_notas,
            'notas_por_libro': notas_por_libro,
            'porcentaje': porcentaje,
            'usuario_meta': usuario_meta,
        })
    if request.method == 'POST':
        form = MetaLecturaForm(request.POST, user=request.user)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.creador = request.user
            meta.save()
            form.save_m2m()
            return redirect('metas:index')
    else:
        form = MetaLecturaForm(user=request.user)
    return render(request, 'metas/index.html', {'form': form, 'progreso': progreso})
from django.urls import path
from . import views

# Create your views here.
