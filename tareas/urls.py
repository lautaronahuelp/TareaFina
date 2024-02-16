from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:pk>/', views.tarea_fina, name='tarea_fina'),
    path('tarea/<int:pk_t>/actividad/<int:pk_a>/completar', views.act_completa, name='act_completa'),
    path('tarea/<int:pk_t>/actividad/agregar', views.act_agregar, name='act_agregar'),
]