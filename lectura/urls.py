from django.urls import path
from . import views

app_name = 'lectura'

urlpatterns = [
    path('', views.LecturaListView.as_view(), name='lista'),  # 👈 esta es la vista principal
    path('progreso/<int:pk>/', views.ProgresoLecturaDetailView.as_view(), name='detalle_progreso'),
    path('progreso/nuevo/<int:libro_id>/', views.ProgresoLecturaCreateView.as_view(), name='crear_progreso'),
    path('progreso/editar/<int:pk>/', views.ProgresoLecturaUpdateView.as_view(), name='editar_progreso'),
]
