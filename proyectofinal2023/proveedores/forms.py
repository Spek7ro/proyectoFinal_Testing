from django import forms
from .models import Proveedor

class FormProveedor(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = '__all__'

        widgets = {
            'RFC': forms.TextInput(
            attrs={'class':'form-class','placeholder':'RFC'}
            ),
            'Razon Social': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Razon Social'}
            ),
            'Direccion': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Dirección'}
            ),
            'Telefono': forms.NumberInput(
            attrs={'class':'form-class','placeholder':'Telefono'}
            ),
            'Correo': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Correo'}
            ),
            'Estado': forms.Select(
            attrs={'class':'form-class', 'placeholder':'Correo'}
            ),
            'Municipio': forms.Select(
            attrs={'class':'form-class', 'placeholder':'Municipio'}
            ),
        }


class FormProveedorEditar(FormProveedor):
    
    class Meta:
        model = Proveedor
        fields = '__all__'