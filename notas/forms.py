from django import forms
from .models import Nota
from libros.models import Libro

class NotaForm(forms.ModelForm):
    libro = forms.ModelChoiceField(queryset=Libro.objects.none(), label='Libro')

    class Meta:
        model = Nota
        fields = ['libro', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu nota aquí...'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['libro'].queryset = Libro.objects.filter(usuario=user)
        else:
            self.fields['libro'].queryset = Libro.objects.none()
