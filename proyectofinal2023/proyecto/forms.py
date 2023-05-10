from django import forms
from .models import Proyecto

class FormProyecto(forms.ModelForm):
    
    class Meta:
        model = Proyecto
        fields = '__all__'

        widgets = {
            'num_proyecto': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'NUM Proyecto'}
            ),
            'nombre_proyecto': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Nombre Proyecto'}
            ),
            'objetivo': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Objetivo'}
            ),
            'presupuesto': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'Presupuesto'}
            ),
            'duracion': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'Duracion'}
            ),
            'responsables': forms.TextInput(
            attrs={'class':'form-class', 'placeholder':'Responsables'}
            ),
            'proveedor': forms.Select(
            attrs= {'class':'form-control'}),
        }


class FormProyectoEditar(FormProyecto):
    
    class Meta:
        model = Proyecto
        exclude = ['num_proyecto']
        
class FiltrosProyecto(FormProyecto):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosProyecto, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False