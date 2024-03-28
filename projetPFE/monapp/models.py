from django.db import models

class Employee(models.Model):
    SEXE_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme')
    ]

    SITUATION_CHOICES = [
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve')
    ]

    sexe = models.CharField(choices=SEXE_CHOICES, max_length=6, verbose_name='Sexe')
    nom = models.CharField(max_length=100, verbose_name='Nom')
    prenom = models.CharField(max_length=100, verbose_name='Prénom')
    date_naissance = models.DateField(verbose_name='Date de Naissance', null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100, verbose_name='Lieu de Naissance', null=True, blank=True)
    situation_familiale = models.CharField(choices=SITUATION_CHOICES, max_length=10, verbose_name='Situation Familiale', null=True, blank=True)
    adresse = models.TextField(verbose_name='Adresse', null=True, blank=True)
    mobile = models.CharField(max_length=20, verbose_name='Mobile', null=True, blank=True)
    telephone = models.CharField(max_length=20, verbose_name='Téléphone', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    diplome_id = models.IntegerField(verbose_name='ID du Diplôme', null=True, blank=True)
    specialite = models.CharField(max_length=100, verbose_name='Spécialité', null=True, blank=True)

    class Meta:
        db_table = 'candidat'  
