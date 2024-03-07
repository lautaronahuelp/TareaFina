from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('<str:category>/', views.lista_tareas, name='lista_tareas_xcat'),
    path('tarea/<int:pk>/', views.tarea_fina, name='tarea_fina'),
    path('tarea/<int:pk_t>/terminar/', views.tarea_terminar, name='tarea_terminar'),
    path('tarea/<int:pk>/editar/', views.tarea_editar, name='tarea_editar'),
    path('tarea/<int:pk_t>/actividad/<int:pk_a>/completar/', views.act_completa, name='act_completa'),
    path('tarea/<int:pk_t>/actividad/agregar/', views.act_agregar, name='act_agregar'),
    path('tarea/agregar/', views.tarea_agregar, name='tarea_agregar'),
    path('tarea/agregar/<int:pk_t>/categoria/', views.tarea_agregar_cat, name='tarea_agregar_cat'),
    path('tarea/agregar/<int:pk_t>/categoria/crear', views.tarea_crear_cat, name='tarea_crear_cat'),
]