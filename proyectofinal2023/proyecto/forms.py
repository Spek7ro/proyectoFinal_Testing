from django import forms
from .models import Proyecto

class FormProyecto(forms.ModelForm):
    
    class Meta:
        model = Proyecto
        fields = '__all__'

        widgets = {
            'NUM Proyecto': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'NUM Proyecto'}
            ),
            'Nombre Proyecto': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Nombre Proyecto'}
            ),
            'Objetivo': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Objetivo'}
            ),
            'Presupuesto': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'Presupuesto'}
            ),
            'Duracion': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'Duracion'}
            ),
            'Responsables': forms.TextInput(
            attrs={'class':'form-class', 'placeholder':'Responsables'}
            ),
            'Proveedor': forms.Select(
            attrs= {'class':'form-control'}),
        }


class FormProyectoEditar(FormProyecto):
    
    class Meta:
        model = Proyecto
        exclude = ['num_proyecto']