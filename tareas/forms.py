from django import forms
from .models import Tarea, Actividad

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ('description', 'deadline_date',)

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('description',)