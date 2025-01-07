from django import forms
from django.contrib.auth.models import User
from .models import DatosPersonalesAlumno,DatosAcademicosAlumno

#FORMS DE DATOS PERSONALES-----------------------------------------------------------------------------------------------
class FormDatosPersonalesAdmin(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "cuenta",
            "calle",
            "numero_exterior",
            "numero_interior",
            "colonia",
            "municipio",
            "codigo_postal",
            "estado",
            "pais",
            "telefono_casa",
            "telefono_movil",
            "genero",
            "correo_1",
            "correo_2",
        ]
        labels = {
            "cuenta": "Usuario",
            "calle": "Calle",
            "numero_exterior": "Número Exterior",
            "numero_interior": "Número Interior",
            "colonia": "Colonia",
            "municipio": "Municipio",
            "codigo_postal": "Código Postal",
            "estado": "Estado",
            "pais": "País",
            "telefono_casa": "Teléfono de Casa",
            "telefono_movil": "Teléfono Móvil",
            "genero": "Género",
            "correo_1": "Correo Electrónico Principal",
            "correo_2": "Correo Electrónico Secundario",
        }
    def __init__(self, *args, **kwargs):
        super(FormDatosPersonalesAdmin, self).__init__(*args, **kwargs)
        self.fields['cuenta'].queryset = User.objects.filter(is_staff=False)
        self.fields['cuenta'].label_from_instance = lambda obj: f" {obj.username} : {obj.first_name} {obj.last_name}"


class FormDatosPersonales(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = [
            "calle",
            "numero_exterior",
            "numero_interior",
            "colonia",
            "municipio",
            "codigo_postal",
            "estado",
            "pais",
            "telefono_casa",
            "telefono_movil",
            "genero",
            "correo_1",
            "correo_2",
        ]
        # widgets = {
        #     "calle" : forms.TextInput(attrs={"class": "form-control"}),
        #     "numero_exterior" : forms.TextInput(attrs={"class": "form-control"}),
        #     "numero_interior" : forms.TextInput(attrs={"class": "form-control"}),
        #     "colonia" : forms.TextInput(attrs={"class": "form-control"}),
        #     "municipio" : forms.TextInput(attrs={"class": "form-control"}),
        #     "codigo_postal" : forms.TextInput(attrs={"class": "form-control"}),
        #     "estado" : forms.TextInput(attrs={"class": "form-control"}),
        #     "pais" : forms.TextInput(attrs={"class": "form-control"}),
        #     "telefono_casa" : forms.TextInput(attrs={"class": "form-control"}),
        #     "telefono_movil" : forms.TextInput(attrs={"class": "form-control"}),
        #     "genero" : forms.Select(attrs={"class": "form-select"}),
        #     "correo_1" : forms.TextInput(attrs={"class": "form-control"}),
        #     "correo_2" : forms.TextInput(attrs={"class": "form-control"}),
        # }
        # labels = {
        #     "calle": "Calle",
        #     "numero_exterior": "Número Exterior",
        #     "numero_interior": "Número Interior",
        #     "colonia": "Colonia",
        #     "municipio": "Municipio",
        #     "codigo_postal": "Código Postal",
        #     "estado": "Estado",
        #     "pais": "País",
        #     "telefono_casa": "Teléfono de Casa",
        #     "telefono_movil": "Teléfono Móvil",
        #     "genero": "Género",
        #     "correo_1": "Correo Electrónico Principal",
        #     "correo_2": "Correo Electrónico Secundario",
        # }

class FormDatosPersonalesCorreo(forms.ModelForm):
    class Meta:
        model = DatosPersonalesAlumno
        fields = ["correo_1"]
        widgets= {"correo_1" : forms.TextInput(attrs={"class": "form-control"})}
        labels = {"correo_1": "Correo Electrónico"}

#FORMS DE DATOS ACADEMICOS-----------------------------------------------------------------------------------------------
class FormDatosAcademicosAdmin(forms.ModelForm):
    class Meta:
        model = DatosAcademicosAlumno
        fields = [
            "cuenta",
            "boleta",
            "unidad_academica_actual",
            "nom_programa_actual",
            "estatus"
        ]
        labels = {
            "cuenta": "Usuario",
            "boleta" : "Boleta",
            "unidad_academica_actual" : "Unidad académica donde está cursando",
            "nom_programa_actual" : "Nombre del programa académico que está cursando",
            "estatus" : "Alumno de"
        }
    def __init__(self, *args, **kwargs):
        super(FormDatosAcademicosAdmin, self).__init__(*args, **kwargs)
        self.fields['cuenta'].queryset = User.objects.filter(is_staff=False)
        self.fields['cuenta'].label_from_instance = lambda obj: f" {obj.username} : {obj.first_name} {obj.last_name}"

class FormDatosAcademicos(forms.ModelForm):
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


class FormDatosAcademicosIns(forms.ModelForm):
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