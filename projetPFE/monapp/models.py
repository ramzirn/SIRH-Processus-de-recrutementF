from django.db import models



from datetime import datetime

from django.db import models

from django.db import models
from django.utils import timezone

from django.db import models

class Annonce(models.Model):
    message_last_post = models.DateTimeField(default='2024-05-31 12:00:00')
    accroche = models.CharField(max_length=255, default='Accroche par défaut')
    desc_societe = models.TextField(default='Description de la société par défaut')
    desc_poste = models.TextField(default='Description du poste par défaut')
    profil_recherche = models.TextField(default='Profil recherché par défaut')
    modalite_reponse = models.CharField(max_length=255, default='Modalités de réponse par défaut')
    obligations = models.TextField(default='Obligations par défaut')
    besoin_id = models.IntegerField(default=0)
    create_uid = models.IntegerField(default=0)
    write_uid = models.IntegerField(default=0)
    activity_date_deadline = models.DateField(default='2024-06-30')
    create_date = models.DateTimeField(default='2024-05-31 12:00:00')
    write_date = models.DateTimeField(default='2024-05-31 12:00:00')

    def __str__(self):
        return self.accroche

    class Meta:
        db_table = 'sirh_annonce'



from django.db import models

from django.db import models
import datetime

from django.db import models

class Besoin(models.Model):
    id = models.AutoField(primary_key=True)
    message_last_post = models.DateTimeField(default='2024-05-31 12:00:00')
    motif = models.CharField(max_length=255, default='')
    pourex = models.IntegerField(default=0)
    budget = models.FloatField(default=0.0)
    intitule = models.IntegerField(default=0)
    echeanceContrat = models.DateField(default='2024-12-31')
    xp = models.IntegerField(default=0)
    lieu = models.CharField(max_length=255, default='')
    deplacement = models.CharField(max_length=255, default='')
    autre = models.CharField(max_length=255, default='')
    dateEntree = models.DateField(default='2024-01-01')
    domaine_ex = models.CharField(max_length=255, default='')
    descr = models.TextField(default='')
    niveau = models.IntegerField(default=0)
    diplome = models.TextField(default='')
    formation = models.TextField(default='')
    formation_oblig = models.TextField(default='')
    savoir_faire = models.TextField(default='')
    savoir_etre = models.TextField(default='')
    type = models.CharField(max_length=255, default='')
    horaires = models.IntegerField(default=0)
    remuneration = models.FloatField(default=0.0)
    create_uid = models.IntegerField(default=1)
    write_uid = models.IntegerField(default=1)
    activity_date_deadline = models.DateField(default='2024-06-30')
    create_date = models.DateTimeField(default='2024-05-31 12:00:00')
    write_date = models.DateTimeField(default='2024-05-31 12:00:00')

    def __str__(self):
        return self.motif

    class Meta:
        db_table = 'sirh_besoin'

   

from django.db import models

class HRJob(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    expected_employees = models.IntegerField()
    no_of_employee = models.IntegerField()
    no_of_recruitment = models.IntegerField()
    no_of_hired_employee = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department_id = models.IntegerField()
    company_id = models.IntegerField()
    state = models.CharField(max_length=255)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField()
    create_date = models.DateTimeField()
    write_uid = models.IntegerField()
    write_date = models.DateTimeField()
    address_id = models.IntegerField()
    manager_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    hr_responsible_id = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'hr_job'
    def __str__(self):
        return self.name



from django.db import models

from django.db import models
import datetime

from datetime import datetime
from django.db import models

class HrApplicant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Nom par défaut')
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    email_from = models.CharField(max_length=128, blank=True, null=True, default='')
    email_cc = models.TextField(blank=True, null=True, default='')
    probability = models.FloatField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(default='2024-01-01 00:00:00')
    write_date = models.DateTimeField(default='2024-01-01 00:00:00')
    stage_id = models.IntegerField(default='1', blank=True, null=True)
    last_stage_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True, default='2024-01-01 00:00:00')
    date_open = models.DateTimeField(blank=True, null=True, default='2024-01-01 00:00:00')
    date_last_stage_update = models.DateTimeField(blank=True, null=True, default='2024-01-01 00:00:00')
    priority = models.CharField(max_length=255, blank=True, null=True, default='')
    job_id = models.IntegerField(blank=True, null=True)
    salary_proposed_extra = models.CharField(max_length=255, blank=True, null=True, default='')
    salary_expected_extra = models.CharField(max_length=255, blank=True, null=True, default='')
    salary_proposed = models.FloatField(blank=True, null=True)
    salary_expected = models.FloatField(blank=True, null=True)
    availability = models.DateField(blank=True, null=True, default='2024-01-01')
    partner_name = models.CharField(max_length=255, blank=True, null=True, default='')
    partner_phone = models.CharField(max_length=32, blank=True, null=True, default='')
    partner_mobile = models.CharField(max_length=32, blank=True, null=True, default='')
    type_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True, default='')
    delay_close = models.FloatField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    campaign_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    medium_id = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True, default='2024-01-01 00:00:00')
    activity_date_deadline = models.DateField(blank=True, null=True, default='2024-01-01')
    create_uid = models.IntegerField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)

    SEXE_CHOICES = [
        ('male', 'Homme'),
        ('female', 'Femme')
    ]
    SITUATION_FAMILIALE_CHOICES = [
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve')
    ]
    CONDITION_PHYSIQUE_CHOICES = [
        ('excellente', 'Excellente'),
        ('bonne', 'Bonne'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
        ('handicap_leger', 'Handicap léger'),
        ('handicap_important', 'Handicap important'),
        ('apte', 'Apte'),
        ('inapte', 'Inapte')
    ]
    STATUS_CHOICES = [
        ('applied', 'Candidature déposée'),
        ('planned', 'Entretient planifié'),
        ('interviewed', 'Entretient effectué'),
        ('rejected', 'Rejetée'),
        ('approved', 'Approuvée')
    ]

    sexe = models.CharField(max_length=20, choices=SEXE_CHOICES, default='female', verbose_name='Sexe')
    date_naissance = models.DateField(verbose_name='Date de Naissance', default='2024-01-01')
    lieu_naissance = models.CharField(max_length=255, verbose_name='Lieu de Naissance', default='')
    situation_familiale = models.CharField(max_length=20, choices=SITUATION_FAMILIALE_CHOICES, verbose_name='Situation Familiale', default='single')
    adresse = models.TextField(verbose_name='Adresse', default='')
    mobile = models.CharField(max_length=20, verbose_name='Mobile', default='')
    email = models.EmailField(verbose_name='Email', default='')
    diplomes = models.TextField(verbose_name='Diplômes', default='')
    specialite = models.CharField(max_length=50, verbose_name='Spécialité', default='')
    exp_prof = models.TextField(verbose_name='Experience professionnelle', default='')
    datedepot = models.DateField(default='2024-01-01', verbose_name='Date dépôt')
    deplacement = models.CharField(max_length=255, verbose_name='Déplacement', default='')
    conditionphysique = models.CharField(max_length=20, choices=CONDITION_PHYSIQUE_CHOICES, verbose_name='Condition Physique', default='apte')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied', verbose_name='État')
    totalpt = models.IntegerField(default=0, verbose_name='Total des points')
    totalgeneral = models.IntegerField(default=0, verbose_name='Total général')

    class Meta:
        db_table = 'hr_applicant'

    def __str__(self):
        return self.name


class RecruitmentDegree(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.IntegerField()
    create_uid = models.IntegerField()
    create_date = models.DateTimeField()
    write_uid = models.IntegerField()
    write_date = models.DateTimeField()

    class Meta:
        db_table = 'hr_recruitment_degree'
        ordering = ['sequence']

    def __str__(self):
        return self.name


from django.db import models

class ResourceCalendar(models.Model):
    name = models.CharField(max_length=255)
    company_id = models.IntegerField()
    create_uid = models.IntegerField()
    create_date = models.DateTimeField()
    write_uid = models.IntegerField()
    write_date = models.DateTimeField()

    class Meta:
        db_table = 'resource_calendar'

    def __str__(self):
        return self.name