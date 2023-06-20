from django import forms
from app.models import Lieu

class LieuForm(forms.ModelForm):
    class Meta:
        model = Lieu
        fields ='__all__'