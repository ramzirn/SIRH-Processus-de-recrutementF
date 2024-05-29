from django.db import models





from django.db import models
from datetime import datetime

from django.db import models

class Annonce(models.Model):
    id = models.AutoField(primary_key=True)
    accroche = models.CharField(max_length=255, default='')
    desc_societe = models.TextField(default='')
    desc_poste = models.TextField(default='')
    profil_recherche = models.TextField(default='')
    modalite_reponse = models.CharField(max_length=255, default='')
    obligations = models.TextField(default='')
    create_uid = models.IntegerField(default=0)
    write_uid = models.IntegerField(default=0)
    message_last_post = models.DateTimeField(default='2000-01-01 00:00:00')
    activity_date_deadline = models.DateField(default='2000-01-01')

    class Meta:
        db_table = 'sirh_annonce'



class Besoin(models.Model):
    motif = models.CharField(max_length=255, blank=True, null=True)
    pourex = models.IntegerField(blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    intitule = models.IntegerField(blank=True, null=True)
    echeanceContrat = models.DateField(blank=True, null=True)
    xp = models.IntegerField(blank=True, null=True)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    deplacement = models.CharField(max_length=255, blank=True, null=True)
    autre = models.CharField(max_length=255, blank=True, null=True)
    dateEntree = models.DateField(blank=True, null=True)
    domaine_ex = models.CharField(max_length=255, blank=True, null=True)
    desc_id = models.IntegerField(blank=True, null=True)
    annonce_id = models.IntegerField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    niveau = models.IntegerField(blank=True, null=True)
    diplome = models.TextField(blank=True, null=True)
    formation = models.TextField(blank=True, null=True)
    formation_oblig = models.TextField(blank=True, null=True)
    savoir_faire = models.TextField(blank=True, null=True)
    savoir_etre = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    horaires = models.IntegerField(blank=True, null=True)
    remuneration = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'sirh_besoin'
   