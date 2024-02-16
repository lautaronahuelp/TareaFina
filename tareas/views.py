from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, Actividad

@login_required
def lista_tareas(request):
    lista = Tarea.objects.filter(author = request.user).order_by('-created_date')
    return render(request, 'tareas/lista_tareas.html', {'lista': lista})

@login_required
def tarea_fina(request, pk):
    tarea = Tarea.objects.get(pk = pk)
    actividades = Actividad.objects.filter(meta = pk).order_by('order')
    return render(request, 'tareas/tarea_fina.html', {'tarea': tarea, 'actividades': actividades})

@login_required
def act_completa(request, pk_t, pk_a):
    actividad = Actividad.objects.get(pk = pk_a)
    actividad.completar()
    return redirect('tarea_fina', pk=pk_t)

@login_required
def act_agregar(request, pk_t):
    return redirect('tarea_fina', pk=pk_t)
