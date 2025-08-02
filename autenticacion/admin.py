from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['correo_electronico', 'username', 'nombre', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nombre', 'correo_electronico')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nombre', 'correo_electronico')}),
    )
    ordering = ['correo_electronico']

admin.site.register(Usuario, UsuarioAdmin)

