from .forms import ProgresoLibroForm
from django.contrib import messages
from django.shortcuts import render
from .models import Libro  # Asegúrate de tener este modelo creado

from .forms import LibroForm
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

def lista_libros(request):
    if request.user.is_superuser or request.user.is_staff:
        libros_propios = Libro.objects.filter(usuario=request.user)
        libros_otros = Libro.objects.exclude(usuario=request.user)
        return render(request, 'libros/lista_libros.html', {
            'libros_propios': libros_propios,
            'libros_otros': libros_otros,
            'es_admin': True
        })
    else:
        libros = Libro.objects.filter(usuario=request.user)
        return render(request, 'libros/lista_libros.html', {'libros': libros, 'es_admin': False})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        form.request = request  # Para que el form pueda acceder al request y procesar nuevas etiquetas
        if form.is_valid():
            form.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm()
        form.request = request
    return render(request, 'libros/crear_libro.html', {'form': form})



def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = ProgresoLibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            # Si tienes un modelo de Progreso, aquí podrías actualizarlo también
            messages.success(request, 'Progreso/estado actualizado correctamente.')
            return redirect('libros:detalle_libro', libro_id=libro.id)
    else:
        form = ProgresoLibroForm(instance=libro)
    return render(request, 'libros/detalle_libro.html', {'libro': libro, 'form_progreso': form})
