from django import forms
from .models import HrApplicant

class CandidateEvaluationForm(forms.ModelForm):
    class Meta:
        model = HrApplicant
        fields = [
            'name',
            'sexe',
            'date_naissance',
            'lieu_naissance',
            'situation_familiale',
            'conditionphysique',
            'adresse',
            'email',
            'mobile',
            'diplomes',
            'specialite',
            'exp_prof',
            'salary_expected_extra',
        ]
        labels = {
            'name':'Nom et prénom',
            'sexe':'Sexe',
            'date_naissance': 'Date de Naissance',
            'lieu_naissance': 'Lieu de Naissance',
            'situation_familiale': 'Situation Familiale',
            'conditionphysique': 'Condition Physique',
            'email': 'Courriel',
            'partner_mobile': 'Mobile',
            'diplomes': 'Diplômes',
            'specialite': 'Spécialité',
            'exp_prof': 'Experience professionnelle',
            'salary_expected_extra': 'Salaire demandé'
        }
        widgets = {
            'sexe': forms.Select(attrs={'class': 'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'situation_familiale': forms.Select(attrs={'class': 'form-control'}),
            'conditionphysique': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'partner_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diplomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'specialite': forms.TextInput(attrs={'class': 'form-control'}),
            'exp_prof': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'salary_expected_extra' :forms.TextInput(attrs={'class': 'form-control'})
        }
