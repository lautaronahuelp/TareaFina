import unicodedata
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea, Actividad, Categoria, Icono
from .forms import ActividadForm, TareaForm, SelCategoriaForm, CategoriaForm

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
def tarea_editar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_agregar_cat', pk_t=tarea.pk)
    else:
        form = TareaForm(instance = tarea)
    return render(request, 'tareas/tarea_editar.html', {'form': form, 'tarea':tarea})


@login_required
def tarea_agregar_cat(request, pk_t):
    tarea = get_object_or_404(Tarea, pk=pk_t)
    if request.method == 'POST':
        form = SelCategoriaForm(request.POST, instance=tarea)
        form.fields['category'].queryset = Categoria.objects.filter(author = request.user) | Categoria.objects.filter(author = 1)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = SelCategoriaForm(instance=tarea)
        form.fields['category'].queryset = Categoria.objects.filter(author = request.user) | Categoria.objects.filter(author = 1)
    return render(request, 'tareas/seleccionar_cat.html', {'form': form, 'tarea':tarea})

@login_required
def tarea_crear_cat(request, pk_t):
    error_desc = ''
    error_icon = ''
    icon_selecc = ''
    tarea = get_object_or_404(Tarea, pk=pk_t)
    iconos = Icono.objects.all()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        norm_description = unicodedata.normalize("NFKD", request.POST['description']).encode("ascii","ignore").decode("ascii").lower()
        check = Categoria.objects.filter(Q(normalized=norm_description) & Q(author=request.user)) | Categoria.objects.filter(Q(normalized=norm_description) & Q(author=1))
        icon = Icono.objects.filter(class_name=request.POST['icon_class'])

        icon_selecc = request.POST['icon_class']

        #errores
        if icon.count() == 0:
            error_icon = 'Icono no válido, seleccione uno de la lista.'
            icon_selecc = ''

        if check.count() == 0:
            form.fields['icon'].required = False
            if form.is_valid() and icon.count() != 0:
                form = form.save(commit=False)
                form.icon = get_object_or_404(Icono, class_name=request.POST['icon_class'])
                form.normalized = norm_description
                form = form.save()
                tareaForm = TareaForm(instance=tarea)
                tareaForm = tareaForm.save(commit=False)
                tareaForm.category = Categoria.objects.get(normalized=norm_description)
                tareaForm.save()
                return redirect('lista_tareas')
        else:
            error_desc = 'El nombre esta en uso, elija otro.'
    else:
        form = CategoriaForm()
     
    return render(request, 'tareas/crear_cat.html', {'form': form, 'tarea': tarea, 'iconos': iconos, 'error_icon': error_icon, 'error_desc': error_desc, 'icon_selecc':icon_selecc})

@login_required
def tarea_terminar(request, pk_t):
    tarea = get_object_or_404(Tarea, pk=pk_t)
    if tarea.completed_date != None:
        if request.method == 'POST':
            
           pass
        else:
            return render(request, 'tareas/tarea_terminar.html')
    
    
    return redirect('tarea_fina', pk=pk_t)