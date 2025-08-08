from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



class RegistroUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Elige un nombre de usuario único. Solo puede contener letras, números y los caracteres @/./+/-/_.'
        self.fields['password1'].help_text = (
            '<ul style="margin:8px 0 0 18px;padding:0;list-style:disc;">'
            '<li>Debe tener al menos 8 caracteres</li>'
            '<li>No puede ser completamente numérica</li>'
            '<li>No debe ser demasiado similar a tus otros datos personales</li>'
            '</ul>'
        )
        self.fields['password2'].help_text = ''
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        return cleaned_data

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        username = self.cleaned_data.get('username') or ''
        nombre = self.cleaned_data.get('nombre') or ''
        correo = self.cleaned_data.get('correo_electronico') or ''
        errores = []
        if password1:
            if len(password1) < 8:
                errores.append('Debe tener al menos 8 caracteres.')
            if password1.isdigit():
                errores.append('No puede ser completamente numérica.')
            if username and username.lower() in password1.lower():
                errores.append('No debe ser demasiado similar a tu nombre de usuario.')
            if nombre and nombre.lower() in password1.lower():
                errores.append('No debe ser demasiado similar a tu nombre.')
            if correo and correo.split('@')[0].lower() in password1.lower():
                errores.append('No debe ser demasiado similar a tu correo electrónico.')
        if errores:
            raise forms.ValidationError(
                '<br>'.join(errores),
                code='invalid_password',
                params=None
            )
        return password1

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'correo_electronico', 'password1', 'password2')
