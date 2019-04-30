from django.db import models
from django.forms import ModelForm

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    articulo = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha_peticion')

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['articulo']
