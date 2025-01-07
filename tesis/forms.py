from django import forms
from .models import ActaRegistroTemaTesis,ActaRevisionTesis,ColegioProfesoresPosgrado

class FormActaRegistroTemaTesis(forms.ModelForm):
    class Meta:
        model = ActaRegistroTemaTesis
        fields = [
            "fecha",
            "unidad_colegio_profesores",
            "nombre_sesion",
            "numero_sesion",
            "fecha_sesion",
            "tema_tesis",
            "objetivo_general_tesis",
            "nombre_director_1",
            "nombre_director_2",
            "aplicacion_director",
            "base_tesis",
            "firma_alumno",
            "firma_director_1",
            "firma_director_2",
            "firma_presidente_colegio"
        ]
        widgets = {
            "fecha" : forms.DateInput(attrs={"class": "mb-2"}),
            "unidad_colegio_profesores": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_sesion": forms.TextInput(attrs={"class": "form-control"}),
            "numero_sesion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_sesion" : forms.DateInput(attrs={"class": "mb-2"}),
            "tema_tesis": forms.TextInput(attrs={"class": "form-control"}),
            "objetivo_general_tesis": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_director_1": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_director_2": forms.TextInput(attrs={"class": "form-control"}),
            "aplicacion_director" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "base_tesis": forms.TextInput(attrs={"class": "form-control"}),
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_director_1" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_director_2" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_presidente_colegio" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }
        labels = {
            "fecha" : "Fecha de la solicitud",
            "unidad_colegio_profesores" : "Colegio de Profesores de Posgrado de ",
            "nombre_sesion" : "Sesión",
            "numero_sesion" : "Número de la Sesión",
            "fecha_sesion" : "Fecha de la Sesión",
            "tema_tesis" : "Tema de la tesis",
            "objetivo_general_tesis" : "Objetivo general de la Tesis",
            "nombre_director_1" : "Nombre del Primer director",
            "nombre_director_2" : "Nombre del Segundo director",
            "aplicacion_director" : "Aplica segundo director",
            "base_tesis" : "Base de la Tesis",
            "firma_alumno" : "Firma del alumno",
            "firma_director_1" : "Firma del primer director",
            "firma_director_2" : "Firma del segundo director",
            "firma_presidente_colegio" : "Firma del presidente del colegio"
        }

class FormColegioProfesoresPosgrado(forms.ModelForm):
    class Meta:
        model = ColegioProfesoresPosgrado
        fields = [
            "unidad_colegio_profesores",
            "nombre_sesion",
            "numero_sesion",
            "fecha_sesion"
        ]
        widgets = {
            "unidad_colegio_profesores": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_sesion": forms.TextInput(attrs={"class": "form-control"}),
            "numero_sesion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_sesion" : forms.DateInput(attrs={"class": "mb-2"}),
        }
        labels = {
            "unidad_colegio_profesores" : "Colegio de Profesores de Posgrado de ",
            "nombre_sesion" : "Sesión",
            "numero_sesion" : "Número de la Sesión",
            "fecha_sesion" : "Fecha de la Sesión"
        }

class FormActaRevisionTemaTesis(forms.ModelForm):
    class Meta:
        model = ActaRevisionTesis
        fields = [
            "fecha",
            "titulo_tesis",
            "porcentaje_plagio",
            "conclusion_plagio",
            "justificacion_conclusion",
            "manifiesto_comision",
            "firma_director_1",
            "firma_director_2",
            "firma_comision_1",
            "firma_comision_2",
            "firma_comision_3",
            "firma_presidente_colegio"
        ]
        widgets = {
            "fecha" : forms.DateInput(attrs={"class": "mb-2"}),
            "titulo_tesis": forms.TextInput(attrs={"class": "form-control"}),
            "porcentaje_plagio": forms.TextInput(attrs={"class": "form-control"}),
            "conclusion_plagio": forms.TextInput(attrs={"class": "form-control"}),
            "justificacion_conclusion": forms.TextInput(attrs={"class": "form-control"}),
            "manifiesto_comision" : forms.Select(attrs={"class": "form-select"}),
            "firma_director_1" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_director_2" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_comision_1" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_comision_2" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_comision_3" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_presidente_colegio" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }
        labels = {
            "fecha" : "Fecha de la solicitud",
            "titulo_tesis" : "Título de la tesis",
            "porcentaje_plagio" : "Porcentaje de plagio",
            "conclusion_plagio" : "Conclusión sobre plagio",
            "justificacion_conclusion" : "Justificación de la conclusión",
            "manifiesto_comision" : "La comisión manifiesta",
            "firma_director_1" : "Firma del primer director",
            "firma_director_2" : "Firma del segundo director",
            "firma_comision_1" : "Firma de la comisión 1",
            "firma_comision_2" : "Firma de la comisión 2",
            "firma_comision_3" : "Firma de la comisión 3",
            "firma_presidente_colegio" : "Firma del presidente del Colegio de profesores"
        }

class FormColegioProfesoresPosgradoRev(forms.ModelForm):
    class Meta:
        model = ColegioProfesoresPosgrado
        fields = ["unidad_colegio_profesores"]
        widgets = {"unidad_colegio_profesores": forms.TextInput(attrs={"class": "form-control"})}
        labels ={"unidad_colegio_profesores":"Colegio de Profesores de Posgrado de "}

