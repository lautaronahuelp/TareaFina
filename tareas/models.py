from django.conf import settings
from django.db import models
from django.utils import timezone

class Color(models.Model):
    description = models.CharField(max_length=50)
    hex_color = models.CharField(max_length=6, default='000000')

    def __str__(self):
        return self.description

class Icono(models.Model):
    description = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Categoria(models.Model):
    description = models.CharField(max_length=50)
    normalized = models.CharField(max_length=50)
    icon = models.ForeignKey(Icono, on_delete=models.CASCADE, null=True, default=None)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, default=None)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description


class Tarea(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, default=None)
    sensation = models.TextField(max_length=255, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    act_total = models.SmallIntegerField(default=0)
    act_completas = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.description
    
    def agregar_act(self):
        if(self.completed_date == None):
            self.act_total += 1
            self.save()

    def completar_act(self):
        if(self.act_completas < self.act_total):
            self.act_completas += 1
            if(self.act_completas == self.act_total):
                self.completed_date = timezone.now()
            self.save()
    
    def estaCompleta(self):
        return self.completed_date != None
    
    def haySensaciones(self):
        return self.sensation != None

class Reaccion(models.Model):
    description = models.CharField(max_length=100)
    emoji = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Actividad(models.Model):
    meta = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    order = models.SmallIntegerField()
    satisfaction = models.ForeignKey(Reaccion, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description
    
    def completar(self, *args, **kwargs):
        if self.completed_date == None:
            self.completed_date = timezone.now()
            self.meta.completar_act()
            super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.meta.agregar_act()
        super().save(*args, **kwargs)

    def estaCompleta(self):
        return self.completed_date != None



