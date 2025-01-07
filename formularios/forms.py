from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *

#FORMS DE ANTEDENTES ACADEMICOS --------------------------------------------------------------------------
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
        labels = {
            "nivel_academico_cursado" : "Nivel académico cursado",
            "programa_academico_cursado" : "Programa académico cursado",
            "institucion_donde_curso" : "Institución donde se cursó",
            "estado_institucion" : "Estado de la república donde se cursó",
            "fecha_graduacion" : "Fecha de graduación (dd/mm/aaaa)"
        }

#FORMS DE SOLICITUDES DE INSCRIPCIÓN --------------------------------------------------------------------------
class FormSolicitudInscripcionAdmin(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = [
            'datos_personales',
            'datos_academicos',
            'fecha',
            'asesor',
            'jefe',
            'firma_alumno',
            'firma_asesor',
            'firma_jefe',
            'aviso_privacidad'
        ]
        labels = {
            'datos_personales':"Datos Personales del alumno" ,
            'datos_academicos':"Datos Académicos del alumno" ,
            'fecha':"Fecha de la solicitud" ,
            'asesor':"Profesor Asesor" ,
            'jefe':"Jefe del Áea" ,
            'firma_alumno':"Firma del alumno" ,
            'firma_asesor':"Firma del asesor" ,
            'firma_jefe':"Firma del jefe de área" ,
            'aviso_privacidad':"Firma del aviso de privacidad"
        }
    def __init__(self, *args, **kwargs):
        super(FormSolicitudInscripcion, self).__init__(*args, **kwargs)
        self.fields['asesor'].queryset = User.objects.filter(is_staff=True)
        self.fields['asesor'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['jefe'].queryset = User.objects.filter(is_staff=True)
        self.fields['jefe'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

class FormSolicitudInscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = [
            'asesor',
            'jefe',
            'firma_alumno',
            'aviso_privacidad'
        ]

class FormSolicitudReinscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudReinscripcion
        fields = [
            "datos_personales",
            "datos_academicos",
            "fecha",
            "periodo",
            "semestre_a_cursar",
            "requiere_unidad",
            "asesor",
            "jefe",
            "firma_alumno",
            "firma_asesor",
            "firma_jefe"
        ]
        labels = {
            'datos_personales':"Datos Personales del alumno" ,
            'datos_academicos':"Datos Académicos del alumno" ,
            'fecha':"Fecha de la solicitud" ,
            "periodo" : "Periodo que va a cursar",
            "semestre_a_cursar" : "Semestre al que se inscribe",
            "requiere_unidad" : "Requiere una unidad de aprendizaje",
            "firma_alumno" : "Firma del alumno",
            "firma_asesor" : "Firma del asesor",
            "firma_jefe" : "Firma del jefe"
        }

    def __init__(self, *args, **kwargs):
        super(FormSolicitudReinscripcion, self).__init__(*args, **kwargs)
        self.fields['asesor'].queryset = User.objects.filter(is_staff=True)
        self.fields['asesor'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['jefe'].queryset = User.objects.filter(is_staff=True)
        self.fields['jefe'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

class FormConstanciaProgramaIndividual(forms.ModelForm):
    class Meta:
        model = ConstanciaProgramaIndividual
        fields =[
            "fecha",
            "fecha_limite",
            "firma_alumno",
            "firma_asesor",
            "firma_jefe"
        ]
        widgets = {
            "fecha_limite" : forms.DateInput(attrs={"class": "mb-2"}),
            "fecha" : forms.DateInput(attrs={"class": "mb-2"}),
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_asesor" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_jefe" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

class FormDatosAcademicosAlumnoTesis(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "boleta",
            "nom_programa_actual"
        ]
        widgets = {
            "boleta" : forms.TextInput(attrs={"class": "form-control"}),
            "nom_programa_actual" : forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "boleta" : "Boleta",
            "unidad_academica_actual" : "Unidad académica donde está cursando"
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
        labels = {
            'is_active': 'Cuenta activa',
            'is_staff': 'Docente',
            'is_superuser': 'Administrador',
        }
        help_texts = {
            'is_active': 'Indica si este usuario está activo en la plataforma.',
            'is_staff': 'Indica si este usuario tiene permisos de docente (firma de documentos).',
            'is_superuser': 'Indica si este usuario es un administrador (para acceso completo, marque también docente)', }

FormsetAntecedentes = forms.formset_factory(FormAntecedentesAcademicos, extra=0)