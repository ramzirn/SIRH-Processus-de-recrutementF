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
   

from django.db import models

class HRJob(models.Model):
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

class HrApplicant(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    email_from = models.CharField(max_length=128, blank=True, null=True)
    email_cc = models.TextField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    partner_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)
    stage_id = models.IntegerField(blank=True, null=True)
    last_stage_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    salary_proposed_extra = models.CharField(max_length=255, blank=True, null=True)
    salary_expected_extra = models.CharField(max_length=255, blank=True, null=True)
    salary_proposed = models.FloatField(blank=True, null=True)
    salary_expected = models.FloatField(blank=True, null=True)
    availability = models.DateField(blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    partner_phone = models.CharField(max_length=32, blank=True, null=True)
    partner_mobile = models.CharField(max_length=32, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    delay_close = models.FloatField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    campaign_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    medium_id = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name