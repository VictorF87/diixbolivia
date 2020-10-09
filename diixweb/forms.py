from django import forms
from .models import votante


class VotanteForm(forms.ModelForm):
    class Meta:
        model = votante
        fields = ['ci', 'celular']
