from django import forms
from app.models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['codeemp', 'nom', 'prenom', 'poste']