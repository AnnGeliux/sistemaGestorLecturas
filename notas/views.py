
from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    notas = Nota.objects.filter(libro__usuario=request.user).order_by('-fecha')
    if request.method == 'POST':
        form = NotaForm(request.POST, user=request.user)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.save()
            return redirect('notas:index')
    else:
        form = NotaForm(user=request.user)
    return render(request, 'notas/index.html', {'form': form, 'notas': notas})

# Create your views here.
