import unicodedata
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea, Actividad, Categoria
from .forms import ActividadForm, TareaForm, SelCategoriaForm

@login_required
def lista_tareas(request, category = None):
    list_category = Categoria.objects.filter(author = request.user) | Categoria.objects.filter(author = 1)
    if category:
        category = unicodedata.normalize("NFKD", category).encode("ascii","ignore").decode("ascii").lower()
        category = get_object_or_404(Categoria, normalized = category)
        cat_pk = category.pk
        lista = Tarea.objects.filter(author = request.user, category = category.pk).order_by('-created_date')
    else:
        lista = Tarea.objects.filter(author = request.user).order_by('-created_date')
        cat_pk = 0
    return render(request, 'tareas/lista_tareas.html', {'lista': lista, 'categorias': list_category, 'cat_pk':cat_pk})

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
            #return redirect('lista_tareas')
            return redirect('tarea_agregar_cat', pk_t=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'tareas/tarea_agregar.html', {'form': form,})

@login_required
def tarea_agregar_cat(request, pk_t):
    tarea = get_object_or_404(Tarea, pk=pk_t)
    if request.method == 'POST':
        form = SelCategoriaForm(request.POST, instance=tarea)
        form.fields['category'].queryset = Categoria.objects.filter(author = request.user) | Categoria.objects.filter(author = 1)
        if form.is_valid():
            tarea = form.save()
            return redirect('lista_tareas')
    else:
        form = SelCategoriaForm(instance=tarea)
        form.fields['category'].queryset = Categoria.objects.filter(author = request.user) | Categoria.objects.filter(author = 1)
    return render(request, 'tareas/seleccionar_cat.html', {'form': form})

@login_required
def tarea_crear_cat(request, pk_t):
    tarea = get_object_or_404(Tarea, pk=pk_t)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
    else:
        form = CategoriaForm()
    return render(request, 'tareas/crear_cat.html', {'form': form, 'tarea': tarea,})