from django import forms
from .models import *

class FormDatosPersonalesAlumno(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "apellido_paterno",
            "apellido_materno",
            "nombre",
            "domicilio",
            "telefono_casa",
            "telefono_movil",
            "sexo",
            "correo_1",
            "correo_2",
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
            "domicilio" : forms.TextInput(attrs={"class": "form-control"}),
            "telefono_casa" : forms.TextInput(attrs={"class": "form-control"}),
            "telefono_movil" : forms.TextInput(attrs={"class": "form-control"}),
            "sexo" : forms.Select(attrs={"class": "form-select"}),
            "correo_1" : forms.TextInput(attrs={"class": "form-control"}),
            "correo_2" : forms.TextInput(attrs={"class": "form-control"}),
        }


class FormDatosAcademicosAlumno(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "boleta",
            "unidad_academica_actual",
            "nom_programa_actual",
            "estatus"
        ]
        widgets = {
            "boleta" : forms.TextInput(attrs={"class": "form-control"}),
            "unidad_academica_actual" : forms.TextInput(attrs={"class": "form-control"}),
            "nom_programa_actual" : forms.TextInput(attrs={"class": "form-control"}),
            "estatus" : forms.Select(attrs={"class": "form-select"})
        }

class FormAntecedentesAcademicos(forms.ModelForm):
    class Meta:
        model = AntecedentesAcademicos
        fields = [
            "nivel_academico_cursado" ,
            "programa_academico_cursado",
            "institucion_donde_curso",
            "estado_institucion",
            "fecha_graduacion"
        ]
        widgets = {
            "nivel_academico_cursado" : forms.Select(attrs={"class": "form-select"}),
            "programa_academico_cursado" : forms.TextInput(attrs={"class": "form-control"}),
            "institucion_donde_curso" : forms.TextInput(attrs={"class": "form-control"}),
            "estado_institucion" : forms.TextInput(attrs={"class": "form-control"}),
            "fecha_graduacion": forms.DateInput(attrs={"class": "mb-2"}),
        }

class FormProgramaSemestral(forms.ModelForm):
    class Meta:
        model = ProgramaSemestral
        fields = [
            "clave",
            "unidad_aprendizaje",
            "profesor",
            "lugar_realizacion"
        ]

        widgets = {
           "clave" : forms.TextInput(attrs={"class": "form-control"}),
            "unidad_aprendizaje" : forms.TextInput(attrs={"class": "form-control"}),
            "profesor" : forms.TextInput(attrs={"class": "form-control"}),
            "lugar_realizacion" : forms.TextInput(attrs={"class": "form-control"}) 
        }

class FormSolicitudInscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = [
            "firma_alumno",
            "firma_asesor",
            "firma_jefe",
            "aviso_privacidad"
        ]

        widgets = {
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_asesor" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_jefe" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "aviso_privacidad" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

FormsetAntecedentes = forms.formset_factory(FormAntecedentesAcademicos, extra=0)
FormsetProgramaIns = forms.formset_factory(FormProgramaSemestral, extra=0)