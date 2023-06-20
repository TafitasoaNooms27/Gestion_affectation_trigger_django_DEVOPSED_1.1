from django import forms
from app.models import Employe, Lieu, Affecter

class AffecterForm(forms.ModelForm):
    class Meta:
        model = Affecter
        fields = '__all__'