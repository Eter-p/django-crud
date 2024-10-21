from django import forms
from .models import *

class FormDatosPersonalesAlumno(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields =[
            "apellido_paterno",
            "apellido_materno",
            "nombre",
            "domicilio",
            "telefono_casa",
            "telefono_movil",
            "sexo",
            "correo_1",
            "correo_2",
            "firma_alumno"
        ]

class FormDatosAcademicosAlumno(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "boleta",
            "unidad_academica_actual",
            "nom_programa_actual",
            "estatus"
        ]

class FormAntecedentesAcademicos(forms.ModelForm):
    class Meta:
        model = AntecedentesAcademicos
        fields = [
            "nivel_academico_cursado",
            "programa_academico_cursado",
            "institucion_donde_curso",
            "estado_institucion",
            "fecha_graduacion"
        ]

class FormProgramaSemestral(forms.ModelForm):
    class Meta:
        model = ProgramaSemestral
        fields = [
            "clave",
            "unidad_aprendizaje",
            "profesor",
            "lugar_realizacion"
        ]

class FormSolicitudInscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = [
            "firma_alumno",
            "firma_asesor",
            "firma_jefe",
            "aviso_privacidad"
        ]