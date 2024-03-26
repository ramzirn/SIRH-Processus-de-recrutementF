from django import forms
from .models import ficheCandidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = ficheCandidat
        fields = '__all__'  