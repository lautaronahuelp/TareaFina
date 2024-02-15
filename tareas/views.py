from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarea, TareaFina

@login_required
def lista_tareas(request):
    lista = Tarea.objects.filter(author = request.user).order_by('-created_date')
    
    return render(request, 'tareas/lista_tareas.html', {'lista': lista})
