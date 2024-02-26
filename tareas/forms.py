from django import forms
from .models import Tarea, Actividad, Categoria, Icono

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N 
    # is True, the locale-dictated format will be applied 
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also: 
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats
     
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M",
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")

class RadioSelectLocalInput(forms.RadioSelect):
    pass

class RadioChoiceLocalField(forms.ModelChoiceField):
    #widget = RadioSelectLocalInput()
    pass

class TareaForm(forms.ModelForm):
    deadline_date = DateTimeLocalField()

    class Meta:
        model = Tarea
        fields = ('description', 'deadline_date',)

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ('description',)

class SelCategoriaForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categoria.objects.none())###LE PASO EL QUERYSET EN LA VIEW 

    class Meta:
        model = Tarea
        fields = ('category',)

class CategoriaForm(forms.ModelForm):
    icon = RadioChoiceLocalField(queryset=Icono.objects.none())
    class Meta:
        model = Categoria
        fields = ('description', 'icon', 'color')