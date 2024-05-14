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
    adresse = models.CharField(verbose_name='Adresse', null=True, blank=True , max_length=1000)
    mobile = models.CharField(max_length=20, verbose_name='Mobile', null=True, blank=True)
    telephone = models.CharField(max_length=20, verbose_name='Téléphone', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    diplome_id = models.IntegerField(verbose_name='ID du Diplôme', null=True, blank=True)
    specialite = models.CharField(max_length=100, verbose_name='Spécialité', null=True, blank=True)

    class Meta:
        db_table = 'candidat'  



from django.db import models
from datetime import datetime

class Annonce(models.Model):

    APPROACH_CHOICES = [
        ('interne', 'Interne'),
        ('externe', 'Externe'),
        ('mixte', 'Mixte')
    ]
    approche = models.CharField(max_length=10, choices=APPROACH_CHOICES, default='interne', verbose_name='Approche de l\'annonce')
    contenu = models.TextField(verbose_name='Contenu de l\'annonce')
    descriptif_societe = models.TextField(default='CETIC', verbose_name='Descriptif rapide de la société')
    profil_recherche = models.TextField(verbose_name='Description du profil recherché')
    MODALITY_CHOICES = [
        ('a', 'E-mail'),
        ('b', 'Telephone'),
    ]
    modalite_reponse = models.CharField(max_length=1, choices=MODALITY_CHOICES, default='a', verbose_name='Modalités de réponse')
    obligations = models.TextField(verbose_name='Obligations')

    class Meta:
        db_table = 'sirh_annonce'

    def __str__(self):
        return self.approche


class Recrutement(models.Model):
   
    MOTIF_CHOICES = [
        ('interne', 'Recrutement interne'),
        ('temp', 'Remplacement temporaire'),
        ('retr', 'Retraite'),
    ]
    motif = models.CharField(max_length=10, choices=MOTIF_CHOICES, verbose_name='Motif de recrutement', null=True, blank=True)
    pourex = models.IntegerField(verbose_name='Pour l\'exercice', default=datetime.now().year)
    intitule = models.CharField(max_length=100, verbose_name='Intitulé du poste')
    budget = models.FloatField(verbose_name='Budget')
    echeanceContrat = models.DateField(verbose_name='Échéance du contrat', null=True, blank=True)
    xp = models.IntegerField(verbose_name='Années d\'expérience')
    lieu = models.CharField(max_length=100, verbose_name='Lieu de travail')
    Deplacement = models.CharField(max_length=100, verbose_name='Déplacement à prévoir', null=True, blank=True)
    autre = models.CharField(max_length=100, verbose_name='Autres aspects à considérer', null=True, blank=True)

    dateEntree = models.DateField(verbose_name="Date d'entrée", null=True, blank=True)
    desc_id = models.CharField(max_length=50, verbose_name='Description', null=True, blank=True)
    annonce_id = models.CharField(max_length=50, verbose_name='Annonce', null=True, blank=True)

    class Meta:
        db_table = 'sirh_besoin'



from django.db import models

class HRJob(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nom du poste')


    class Meta:
        db_table = 'hr_job'
     

    def __str__(self):
        return self.name



from django.db import models

class Description(models.Model):

    intitule = models.CharField(max_length=100, verbose_name='Intitulé du poste')
    descr = models.TextField(verbose_name='Description du poste')
    niveau_choices = [
        ('bac', 'Baccalauréat'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat'),
    ]
    niveau = models.CharField(max_length=20, choices=niveau_choices, verbose_name="Niveau d'étude")
    diplome = models.CharField(max_length=1, choices=[('g', 'f')], verbose_name="Diplôme")
    formation = models.CharField(max_length=1, choices=[('g', 'f')], verbose_name="Formation")
    formation_experience = models.CharField(max_length=1, choices=[('g', 'f')], verbose_name="Formation liée à l'expérience du poste")
    savoir_faire = models.TextField(verbose_name="Savoir-faire")
    savoir_etre = models.TextField(verbose_name="Savoir-être")
    type_choices = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ]
    type = models.CharField(max_length=3, choices=type_choices, default='CDI', verbose_name='Type de contrat')
    horaires = models.CharField(max_length=100, verbose_name='Horaires de travail', null=True, blank=True)
    remuneration = models.FloatField(verbose_name='Rémunération', default=0)

    class Meta:
        db_table ='sirh_desc'
        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        return self.intitule
