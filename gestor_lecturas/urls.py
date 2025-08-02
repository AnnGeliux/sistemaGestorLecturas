"""
URL configuration for gestor_lecturas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
    path('lectura/', include('lectura.urls')),
    path('metas/', include('metas.urls')),
    path('notas/', include('notas.urls')),
    path('estadisticas/', include('estadisticas.urls')),
    path('autenticacion/', include('autenticacion.urls')),

    path('dashboard/', dashboard, name='dashboard'),
    # Redirigir la raíz al login
    path('', lambda request: redirect('login'), name='home'),
]

