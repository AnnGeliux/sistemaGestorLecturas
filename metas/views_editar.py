from django.shortcuts import render, redirect, get_object_or_404
from .models import MetaLectura
from .forms import MetaLecturaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def editar_meta(request, pk):
    meta = get_object_or_404(MetaLectura, pk=pk)
    # Permitir que solo el creador o un admin edite la meta
    if meta.creador != request.user and not (request.user.is_superuser or request.user.is_staff):
        return HttpResponseForbidden('No tienes permiso para editar esta meta.')
    if request.method == 'POST':
        form = MetaLecturaForm(request.POST, instance=meta, user=request.user)
        if form.is_valid():
            meta = form.save(commit=False)
            # Guardar los campos extra objetivo_libros y objetivo_notas
            meta.objetivo_libros = form.cleaned_data.get('objetivo_libros')
            meta.objetivo_notas = form.cleaned_data.get('objetivo_notas')
            meta.save()
            form.save_m2m()
            return redirect('metas:index')
    else:
        form = MetaLecturaForm(instance=meta, user=request.user)
    return render(request, 'metas/editar_meta.html', {'form': form, 'meta': meta})
