from django import forms
from .models import CuentaBancaria

class FormCuentaBancaria(forms.ModelForm):
    
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

        widgets = {
            'idcuenta': forms.TextInput(
                attrs={'class':'form-class','placeholder':'ID cuenta'}
            ),
            'responsable': forms.TextInput(
                attrs={'class':'form-class','placeholder':'Responsable'}
            ),
            'limite_presupuestario': forms.TextInput(
                attrs={'class':'form-class','placeholder':'Limite presupuestario'}
            ),
            'proyecto': forms.Select(
            attrs= {'class':'form-control'}),
        }


class FormCuentaBancariaEditar(FormCuentaBancaria):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'
        
class FiltrosCuenta(FormCuentaBancaria):
    
    def __init__(self, *args, **kwargs):
        super(FiltrosCuenta, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].required = False