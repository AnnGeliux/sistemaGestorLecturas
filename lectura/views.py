from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import ProgresoLectura
from libros.models import Libro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class ProgresoLecturaCreateView(LoginRequiredMixin, CreateView):
    model = ProgresoLectura
    fields = ['ultima_pagina_leida']
    template_name = 'lectura/progreso_form.html'

    def form_valid(self, form):
        libro = get_object_or_404(Libro, pk=self.kwargs['libro_id'])
        form.instance.libro = libro
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lectura:detalle_progreso', kwargs={'pk': self.object.pk})

class ProgresoLecturaUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgresoLectura
    fields = ['ultima_pagina_leida']
    template_name = 'lectura/progreso_form.html'

    def get_success_url(self):
        return reverse_lazy('lectura:detalle_progreso', kwargs={'pk': self.object.pk})

class ProgresoLecturaDetailView(LoginRequiredMixin, DetailView):
    model = ProgresoLectura
    template_name = 'lectura/progreso_detalle.html'
class LecturaListView(LoginRequiredMixin, ListView):
    model = ProgresoLectura
    template_name = 'lectura/lista.html'
    context_object_name = 'progresos'

    def get_queryset(self):
        return ProgresoLectura.objects.filter(libro__usuario=self.request.user)
