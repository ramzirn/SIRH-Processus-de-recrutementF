# Generated by Django 3.2.25 on 2024-05-30 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0010_auto_20240530_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrapplicant',
            name='adresse',
            field=models.TextField(default='', verbose_name='Adresse'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='conditionphysique',
            field=models.CharField(choices=[('excellente', 'Excellente'), ('bonne', 'Bonne'), ('moyenne', 'Moyenne'), ('faible', 'Faible'), ('handicap_leger', 'Handicap léger'), ('handicap_important', 'Handicap important'), ('apte', 'Apte'), ('inapte', 'Inapte')], default='apte', max_length=20, verbose_name='Condition Physique'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date de Naissance'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='datedepot',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Date dépôt'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='deplacement',
            field=models.CharField(default='', max_length=255, verbose_name='Déplacement'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='diplomes',
            field=models.TextField(default='', verbose_name='Diplômes'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='exp_prof',
            field=models.TextField(default='', verbose_name='Experience professionnelle'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='lieu_naissance',
            field=models.CharField(default='', max_length=255, verbose_name='Lieu de Naissance'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='mobile',
            field=models.CharField(default='', max_length=20, verbose_name='Mobile'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='sexe',
            field=models.CharField(choices=[('male', 'Homme'), ('female', 'Femme')], default='female', max_length=20, verbose_name='Sexe'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='situation_familiale',
            field=models.CharField(choices=[('single', 'Célibataire'), ('married', 'Marié(e)'), ('divorced', 'Divorcé(e)'), ('widowed', 'Veuf/Veuve')], default='single', max_length=20, verbose_name='Situation Familiale'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='specialite',
            field=models.CharField(default='', max_length=50, verbose_name='Spécialité'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='status',
            field=models.CharField(choices=[('applied', 'Candidature déposée'), ('planned', 'Entretient planifié'), ('interviewed', 'Entretient effectué'), ('rejected', 'Rejetée'), ('approved', 'Approuvée')], default='applied', max_length=20, verbose_name='État'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='totalgeneral',
            field=models.IntegerField(default=0, verbose_name='Total général'),
        ),
        migrations.AddField(
            model_name='hrapplicant',
            name='totalpt',
            field=models.IntegerField(default=0, verbose_name='Total des points'),
        ),
        migrations.AlterModelTable(
            name='hrapplicant',
            table='hr_applicant',
        ),
    ]