from django import forms
from .models import Proveedor


class FormProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'

        widgets = {
            'rfc': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'RFC'}
            ),
            'razon_social': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'Razon Social'}
            ),
            'direccion': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'Dirección'}
            ),
            'telefono': forms.NumberInput(
                attrs={'class': 'form-class', 'placeholder': 'Telefono'}
            ),
            'correo': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'Correo'}
            ),
            'estado': forms.Select(
                attrs={'class': 'form-class', 'placeholder': 'Estado'}
            ),
            'municipio': forms.Select(
                attrs={'class': 'form-class', 'placeholder': 'Municipio'}
            ),
        }


class FormProveedorEditar(FormProveedor):

    class Meta:
        model = Proveedor
        fields = '__all__'


class FiltrosProveedor(FormProveedor):

    def __init__(self, *args, **kwargs):
        super(FiltrosProveedor, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
