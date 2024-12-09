from django import forms
from .models import *

class FormDatosPersonalesAlumnoIns(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "apellido_paterno",
            "apellido_materno",
            "nombre",
            "calle",
            "numero_exterior",
            "numero_interior",
            "colonia",
            "municipio",
            "codigo_postal",
            "estado",
            "telefono_casa",
            "telefono_movil",
            "genero",
            "correo_1",
            "correo_2",
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
            "calle" : forms.TextInput(attrs={"class": "form-control"}),
            "numero_exterior" : forms.TextInput(attrs={"class": "form-control"}),
            "numero_interior" : forms.TextInput(attrs={"class": "form-control"}),
            "colonia" : forms.TextInput(attrs={"class": "form-control"}),
            "municipio" : forms.TextInput(attrs={"class": "form-control"}),
            "codigo_postal" : forms.TextInput(attrs={"class": "form-control"}),
            "estado" : forms.TextInput(attrs={"class": "form-control"}),
            "telefono_casa" : forms.TextInput(attrs={"class": "form-control"}),
            "telefono_movil" : forms.TextInput(attrs={"class": "form-control"}),
            "genero" : forms.Select(attrs={"class": "form-select"}),
            "correo_1" : forms.TextInput(attrs={"class": "form-control"}),
            "correo_2" : forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "apellido_paterno": "Apellido Paterno",
            "apellido_materno": "Apellido Materno",
            "nombre": "Nombre",
            "calle": "Calle",
            "numero_exterior": "Número Exterior",
            "numero_interior": "Número Interior",
            "colonia": "Colonia",
            "municipio": "Municipio",
            "codigo_postal": "Código Postal",
            "estado": "Estado",
            "telefono_casa": "Teléfono de Casa",
            "telefono_movil": "Teléfono Móvil",
            "genero": "Género",
            "correo_1": "Correo Electrónico Principal",
            "correo_2": "Correo Electrónico Secundario",
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
        labels = {
            "unidad_academica_actual": "Unidad acdemica actual",
            "nom_programa_actual": "Nombre del programa académico que esta cursando",
            "estatus": "Alumno de tiempo",
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
        labels = {
            "nivel_academico_cursado" : "Nivel académico cursado",
            "programa_academico_cursado" : "Programa académico cursado",
            "institucion_donde_curso" : "Institución donde se cursó",
            "estado_institucion" : "Estado de la república donde se cursó",
            "fecha_graduacion" : "Fecha de graduación (dd/mm/aaaa)"
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
            "clave" : forms.Select(attrs={"class": "form-select"}),
            "unidad_aprendizaje" : forms.Select(attrs={"class": "form-select"}),
            "profesor" : forms.TextInput(attrs={"class": "form-control"}),
            "lugar_realizacion" : forms.TextInput(attrs={"class": "form-control"}) 
        }
        labels = {
            "clave": "Clave de la unidad de aprendizaje ",
            "unidad_aprendizaje": "Unidad de aprendizaje",
            "profesor": "Profesor",
            "lugar_realizacion": "Institución donde se cursará"
        }

class FormSolicitudInscripcion(forms.ModelForm):
    class Meta:
        model = SolicitudInscripcion
        fields = [
            "fecha",
            "firma_alumno",
            "firma_asesor",
            "firma_jefe",
            "aviso_privacidad"
        ]

        widgets = {
            "fecha": forms.DateInput(attrs={"class": "mb-2"}),
            "firma_alumno" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_asesor" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "firma_jefe" : forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "aviso_privacidad" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }
        labels = {
            "fecha": "Fecha (dd/mm/aaaa)",
            "firma_alumno" : "Firma del alumno",
            "firma_asesor" : "Firma del asedor",
            "firma_jefe" : "Firma del jefe",
            "aviso_privacidad" : "Aviso de privacida"
        }

class FormDatosPersonalesAlumnoRei(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "apellido_paterno",
            "apellido_materno",
            "nombre",
            "correo_1"
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
            "correo_1" : forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            "apellido_paterno": "Apellido Paterno",
            "apellido_materno": "Apellido Materno",
            "nombre": "Nombre",
            "correo_1": "Correo Electrónico "
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
        labels = {
            "boleta" : "Boleta",
            "unidad_academica_actual" : "Unidad académica donde está cursando",
            "nom_programa_actual" : "Nombre del programa académico que está cursando",
            "estatus" : "Alumno de tiempo"
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
        labels = {
            "fecha" : "Fecha de la solicitud",
            "periodo" : "Periodo que va a cursar",
            "semestre_a_cursar" : "Semestre al que se inscribe",
            "requiere_unidad" : "Requiere una unidad de aprendizaje",
            "firma_alumno" : "Firma del alumno",
            "firma_asesor" : "Firma del asesor",
            "firma_jefe" : "Firma del jefe"
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
            "nombre"
        ]
        widgets = {
            "apellido_paterno" : forms.TextInput(attrs={"class": "form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class": "form-control"}),
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "apellido_paterno": "Apellido Paterno",
            "apellido_materno": "Apellido Materno",
            "nombre": "Nombre",
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
        labels = {
            "clave" : "Clave de la unidad de aprendizaje",
            "unidad_aprendizaje" : "Unidad de aprendizaje",
            "creditos" : "Créditos de la unidad",
            "periodo" : "Periodo de realización",
            "lugar_realizacion" : "Lugar de realización"
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
        labels = {
            "fecha" : "Fecha de la solicitud",
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

FormsetAntecedentes = forms.formset_factory(FormAntecedentesAcademicos, extra=0)
FormsetProgramaSem = forms.formset_factory(FormProgramaSemestral, extra=0)
FormsetProgramaInd = forms.formset_factory(FormProgramaActividades, extra=0)