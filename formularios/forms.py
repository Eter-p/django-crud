from django import forms
from .models import *

class FormDatosPersonalesAlumnoIns(forms.ModelForm):
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


class FormDatosAcademicosAlumnoIns(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "unidad_academica_actual",
            "nom_programa_actual",
            "estatus"
        ]
        widgets = {
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

class FormDatosPersonalesAlumnoRei(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "apellido_paterno",
            "apellido_materno",
            "nombre",
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
        }

class FormDatosAcademicosAlumnoRei(forms.ModelForm):
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

class FormSolicitudReinscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudReinscripcion
        fields = [
            "fecha",
            "periodo",
            "semestre_a_cursar",
            "requiere_unidad",
            "firma_alumno",
            "firma_asesor",
            "firma_jefe"
        ]
        widgets = {
            "fecha" : forms.DateInput(attrs={"class": "mb-2"}),
            "periodo": forms.TextInput(attrs={"class": "form-control"}),
            "semestre_a_cursar" : forms.Select(attrs={"class": "form-select"}),
            "requiere_unidad" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_asesor" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_jefe" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }


class FormConstanciaProgramaIndividual(forms.ModelForm):
    class Meta:
        model = ConstanciaProgramaIndividual
        fields =[
            "fecha",
            "total_creditos",
            "fecha_limite",
            "firma_alumno",
            "firma_asesor",
            "firma_jefe"
        ]
        widgets = {
            "total_creditos" : forms.TextInput(attrs={"class": "form-control"}),
            "fecha_limite" : forms.DateInput(attrs={"class": "mb-2"}),
            "fecha" : forms.DateInput(attrs={"class": "mb-2"}),
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_asesor" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_jefe" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

class FormDatosAsesor(forms.ModelForm):
    class Meta:
        model = DatosAsesor
        fields = [
            "apellido_paterno",
            "apellido_materno",
            "nombre",
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
        }

class FormProgramaActividades(forms.ModelForm):
    class Meta:
        model = ProgramaActividades
        fields = [
            "clave",
            "unidad_aprendizaje",
            "creditos",
            "periodo",
            "lugar_realizacion"
        ]

        widgets = {
            "clave" : forms.TextInput(attrs={"class": "form-control"}),
            "unidad_aprendizaje" : forms.TextInput(attrs={"class": "form-control"}),
            "creditos" : forms.TextInput(attrs={"class": "form-control"}),
            "periodo" : forms.Select(attrs={"class": "form-select"}),
            "lugar_realizacion" : forms.TextInput(attrs={"class": "form-control"})
        }

class FormDatosAcademicosAlumnoTesis(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "boleta",
            "nom_programa_actual",
        ]
        widgets = {
            "boleta" : forms.TextInput(attrs={"class": "form-control"}),
            "nom_programa_actual" : forms.TextInput(attrs={"class": "form-control"}),
        }

class FormActaRegistroTemaTesis(forms.ModelForm):
    class Meta:
        model = ActaRegistroTemaTesis
        fields = [
            "fecha",
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

class FormColegioProfesoresPosgradoRev(forms.ModelForm):
    class Meta:
        model = ColegioProfesoresPosgrado
        fields = ["unidad_colegio_profesores"]
        widgets = {"unidad_colegio_profesores": forms.TextInput(attrs={"class": "form-control"})}

FormsetAntecedentes = forms.formset_factory(FormAntecedentesAcademicos, extra=0)
FormsetProgramaSem = forms.formset_factory(FormProgramaSemestral, extra=0)
FormsetProgramaInd = forms.formset_factory(FormProgramaActividades, extra=0)