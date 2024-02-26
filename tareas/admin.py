from django.contrib import admin
from .models import Tarea, Actividad, Reaccion, Categoria, Icono, Color

admin.site.register(Tarea)
admin.site.register(Actividad)
admin.site.register(Reaccion)
admin.site.register(Categoria)
admin.site.register(Icono)
admin.site.register(Color)