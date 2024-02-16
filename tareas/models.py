from django.conf import settings
from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    sensation = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    act_total = models.SmallIntegerField(default=0)
    act_completas = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.description

    def completar_act(self):
        if(self.act_completas < self.act_total):
            self.act_completas += 1
            self.save()
    
    def agregar_act(self):
        if(self.completed_date == None):
            self.act_total += 1
            self.save()

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
        self.completed_date = timezone.now()
        self.meta.completar_act()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.meta.agregar_act()
        super().save(*args, **kwargs)



