from django import forms
from .models import Costo


class FormCosto(forms.ModelForm):

    class Meta:
        model = Costo
        fields = '__all__'

        widgets = {

            'descripcion': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'Descripcion'}
            ),
            'costo': forms.NumberInput(
                attrs={'class': 'form-class', 'placeholder': 'Costo'}
            ),
            'proyecto': forms.TextInput(
                attrs={'class': 'form-class', 'placeholder': 'Proyecto'}
            ),
        }


class FormCostoEditar(FormCosto):

    class Meta:
        model = Costo
        exclude = ['id']


class FiltrosCosto(FormCosto):

    def __init__(self, *args, **kwargs):
        super(FiltrosCosto, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
