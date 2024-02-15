from django.conf import settings
from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    sensation = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description

class Reaccion(models.Model):
    description = models.CharField(max_length=100)
    emoji = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class TareaFina(models.Model):
    meta = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    order = models.SmallIntegerField()
    satisfaction = models.ForeignKey(Reaccion, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description
    
    def complete(self):
        self.completed_date = timezone.now()
        self.save()



