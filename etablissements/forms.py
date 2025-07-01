
from django import forms
from .models import Etablissement, Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'

class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissement
        fields = '__all__'