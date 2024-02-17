from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea, Actividad
from .forms import ActividadForm, TareaForm

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
    order = Actividad.objects.filter(meta = pk_t).count() + 1
    tarea = Tarea.objects.get(pk=pk_t)
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.meta = tarea
            actividad.order = order
            actividad.save()
            return redirect('tarea_fina', pk = pk_t)
    else:
        form = ActividadForm()
    return render(request, 'tareas/act_agregar.html', {'form': form, 'tarea': tarea, 'pk_t': pk_t, })

@login_required
def tarea_agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.author = request.user
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_agregar.html', {'form': form,})