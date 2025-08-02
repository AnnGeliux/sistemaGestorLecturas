
from django.urls import path

from . import views
from . import views_editar

app_name = 'metas'

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:pk>/', views_editar.editar_meta, name='editar_meta'),
]
