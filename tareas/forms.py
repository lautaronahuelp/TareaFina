from django import forms
from .models import Tarea, Actividad

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    #HACER PRUEBAS CON FIREFOX Y EDITANDO UN OBJETO EXISTENTE
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N 
    # is True, the locale-dictated format will be applied 
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also: 
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats
     
    #input_formats = [
    #    "%Y-%m-%dT%H:%M:%S", 
    #    "%Y-%m-%dT%H:%M:%S.%f", 
    #    "%Y-%m-%dT%H:%M",
    #]
    #widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")
    widget = DateTimeLocalInput()
    #widget = forms.SplitDateTimeWidget()

class TareaForm(forms.ModelForm):
    deadline_date = DateTimeLocalField()

    class Meta:
        model = Tarea
        fields = ('description', 'deadline_date',)

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('description',)