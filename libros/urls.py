
from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('nuevo/', views.crear_libro, name='crear_libro'),
    path('<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
]
