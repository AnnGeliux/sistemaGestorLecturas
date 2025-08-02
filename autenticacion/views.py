from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm
from libros.models import Libro
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'autenticacion/login.html'
    redirect_authenticated_user = True
    extra_context = {'title': 'Iniciar sesión'}
    def get_success_url(self):
        return '/dashboard/'
@login_required
def dashboard(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'autenticacion/dashboard.html', {'libros': libros})
from django.contrib.auth.admin import UserAdmin

# Vista de registro de usuario
def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'autenticacion/register.html', {'form': form})
