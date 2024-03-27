from django.db import models

class Employee(models.Model):
    sexe_choices = [('male', 'Homme'), ('female', 'Femme')]
    situation_familiale_choices = [
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve')
    ]
    diplome_choices = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
        ('other', 'Autre')
    ]

    sexe = models.CharField(choices=sexe_choices, max_length=6, verbose_name='Sexe')
    nom = models.CharField(max_length=100, verbose_name='Nom')
    prenom = models.CharField(max_length=100, verbose_name='Prénom')
    date_naissance = models.DateField(verbose_name='Date de Naissance')
    lieu_naissance = models.CharField(max_length=100, verbose_name='Lieu de Naissance')
    situation_familiale = models.CharField(choices=situation_familiale_choices, max_length=10, verbose_name='Situation Familiale')
    adresse = models.TextField(verbose_name='Adresse')
    mobile = models.CharField(max_length=20, verbose_name='Mobile')
    telephone = models.CharField(max_length=20, verbose_name='Téléphone')
    email = models.EmailField(verbose_name='Email')
    diplome = models.CharField(choices=diplome_choices, max_length=10, verbose_name='Diplôme', null=True, blank=True)

    specialite = models.CharField(max_length=100, verbose_name='Spécialité')

    def __str__(self):
        return f"{self.nom} {self.prenom}"
