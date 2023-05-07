from django import forms
from .models import CuentaBancaria

class FormCuentaBancaria(forms.ModelForm):
    
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

        widgets = {
            'Proyecto': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Proyecto'}
            ),
            'Responsable': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Responsable'}
            ),
            'Limite presupuestario': forms.TextInput(
            attrs={'class':'form-class','placeholder':'Limite presupuestario'}
            ),
        }


class FormCuentaBancariaEditar(FormCuentaBancaria):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'