from django import forms
from .models import MetaLectura
from libros.models import Libro

class MetaLecturaForm(forms.ModelForm):
    objetivo_libros = forms.IntegerField(required=False, min_value=1, label='Objetivo de libros leídos')
    objetivo_notas = forms.IntegerField(required=False, min_value=1, label='Objetivo de notas por libro')

    class Meta:
        model = MetaLectura
        fields = ['nombre', 'tipo', 'fecha_inicio', 'fecha_fin', 'libros_asociados', 'usuarios_asignados']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'libros_asociados': forms.SelectMultiple(attrs={'size': 5}),
            'usuarios_asignados': forms.SelectMultiple(attrs={'size': 5}),
        }

    def __init__(self, *args, **kwargs):
        from autenticacion.models import Usuario
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['libros_asociados'].required = False
        if user:
            self.fields['libros_asociados'].queryset = Libro.objects.filter(usuario=user)
            # Solo los admins pueden asignar metas a cualquier usuario
            if user.is_superuser or user.is_staff:
                self.fields['usuarios_asignados'].queryset = Usuario.objects.all()
            else:
                # Usuarios normales solo pueden asignar metas a sí mismos y a otros usuarios normales (no admins)
                self.fields['usuarios_asignados'].queryset = Usuario.objects.filter(is_superuser=False, is_staff=False)
        else:
            self.fields['libros_asociados'].queryset = Libro.objects.none()
            self.fields['usuarios_asignados'].queryset = self.fields['usuarios_asignados'].queryset.none()
