from django import forms
from django.contrib.auth.models import User
from .models import ProgramaSemestral,InscripcionPrograma

class FormProgramaSemestral(forms.ModelForm):
    class Meta:
        model = ProgramaSemestral
        fields = ['unidad_aprendizaje', 'profesor', 'lugar_realizacion']

    def __init__(self, *args, **kwargs):
        super(FormProgramaSemestral, self).__init__(*args, **kwargs)
        self.fields['profesor'].queryset = User.objects.filter(is_staff=True)
        self.fields['profesor'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"

class FormPrograma(forms.ModelForm):
    class Meta:
        model = InscripcionPrograma
        fields = ["id_programa_semestral"]
        widgets = {
            "id_programa_semestral" : forms.Select(attrs={"class": "form-select"})
        }
        labels = {
            "id_programa_semestral" : "Unidad de aprendizaje"
        }

FormsetProgramaSem = forms.formset_factory(FormPrograma, extra=0)
