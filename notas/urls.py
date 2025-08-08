
from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nota_id>/editar/', views.editar_nota, name='editar_nota'),
    path('<int:nota_id>/eliminar/', views.eliminar_nota, name='eliminar_nota'),
]
