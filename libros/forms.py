
from django import forms
from .models import Libro, Categoria, Etiqueta

class ProgresoLibroForm(forms.ModelForm):
    porcentaje_avance = forms.IntegerField(label="Progreso (%)", min_value=0, max_value=100, required=True)
    estado = forms.ChoiceField(choices=Libro.ESTADOS, label="Estado del libro", required=True)

    class Meta:
        model = Libro
        fields = ['estado', 'porcentaje_avance']

class CategoriaWidget(forms.TextInput):
    """Widget para permitir crear una nueva categoría desde el formulario."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({'placeholder': 'Escribe una nueva categoría o selecciona una'})



class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2101)),
        required=False,
        label='Fecha de publicación'
    )
    nueva_categoria = forms.CharField(
        required=False,
        label='Nueva categoría',
        widget=CategoriaWidget
    )
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': 5}),
        label='Etiquetas (opcional)'
    )

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoría',
        empty_label='Selecciona una categoría (opcional)'
    )

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'numero_paginas', 'estado', 'categoria', 'nueva_categoria', 'etiquetas', 'fecha_publicacion', 'usuario']

    def clean(self):
        cleaned_data = super().clean()
        nueva_categoria = cleaned_data.get('nueva_categoria')
        if nueva_categoria:
            categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            cleaned_data['categoria'] = categoria
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Asignar la categoría creada si corresponde
        nueva_categoria = self.cleaned_data.get('nueva_categoria')
        if nueva_categoria:
            categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            instance.categoria = categoria
        if commit:
            instance.save()
            self.save_m2m()
        # Procesar nuevas etiquetas dinámicas
        request = getattr(self, 'request', None)
        if request:
            nuevas_etiquetas = request.POST.getlist('nueva_etiqueta')
            for nombre in nuevas_etiquetas:
                nombre = nombre.strip()
                if nombre:
                    etiqueta, created = Etiqueta.objects.get_or_create(nombre=nombre)
                    instance.etiquetas.add(etiqueta)
        return instance
