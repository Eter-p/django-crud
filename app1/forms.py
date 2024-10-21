from django import forms
from .models import Task

# forms.py
from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(label='Teléfono', max_length=15)
