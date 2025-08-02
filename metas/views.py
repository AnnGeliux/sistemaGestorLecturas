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
        total_libros = meta.libros_asociados.count()
        libros_leidos = meta.libros_asociados.filter(estado='leido').count()
        objetivo_libros = getattr(meta, 'objetivo_libros', None)
        objetivo_notas = getattr(meta, 'objetivo_notas', None)
        notas_por_libro = {}
        if objetivo_notas:
            for libro in meta.libros_asociados.all():
                notas = Nota.objects.filter(libro=libro).count()
                notas_por_libro[libro.titulo] = notas
        progreso.append({
            'meta': meta,
            'total_libros': total_libros,
            'libros_leidos': libros_leidos,
            'objetivo_libros': objetivo_libros,
            'objetivo_notas': objetivo_notas,
            'notas_por_libro': notas_por_libro,
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
