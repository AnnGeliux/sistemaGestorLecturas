
# Vista para editar una nota
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Nota
from .forms import NotaForm

@login_required
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id, libro__usuario=request.user)
    # El usuario puede eliminar cualquier nota de sus propios libros
    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada correctamente.')
        return redirect('notas:index')
    return render(request, 'notas/eliminar_nota.html', {'nota': nota})

@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id, libro__usuario=request.user)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota actualizada correctamente.')
            return redirect('notas:index')
    else:
        form = NotaForm(instance=nota, user=request.user)
    return render(request, 'notas/editar_nota.html', {'form': form, 'nota': nota})

@login_required
def index(request):
    notas = Nota.objects.filter(autor=request.user).order_by('-fecha')
    if request.method == 'POST':
        form = NotaForm(request.POST, user=request.user)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.autor = request.user
            nota.save()
            return redirect('notas:index')
    else:
        form = NotaForm(user=request.user)
    return render(request, 'notas/index.html', {'form': form, 'notas': notas})
