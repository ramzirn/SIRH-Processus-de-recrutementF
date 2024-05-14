# Generated by Django 3.2.25 on 2024-04-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruitment_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Recrutement')),
                ('description_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Description')),
                ('approche', models.CharField(choices=[('interne', 'Interne'), ('externe', 'Externe'), ('mixte', 'Mixte')], default='interne', max_length=10, verbose_name="Approche de l'annonce")),
                ('contenu', models.TextField(verbose_name="Contenu de l'annonce")),
                ('descriptif_societe', models.TextField(default='CETIC', verbose_name='Descriptif rapide de la société')),
                ('profil_recherche', models.TextField(verbose_name='Description du profil recherché')),
                ('modalite_reponse', models.CharField(choices=[('a', 'E-mail'), ('b', 'Telephone')], default='a', max_length=1, verbose_name='Modalités de réponse')),
                ('obligations', models.TextField(verbose_name='Obligations')),
            ],
            options={
                'db_table': 'sirh_annonce',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('male', 'Homme'), ('female', 'Femme')], max_length=6, verbose_name='Sexe')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('date_naissance', models.DateField(blank=True, null=True, verbose_name='Date de Naissance')),
                ('lieu_naissance', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lieu de Naissance')),
                ('situation_familiale', models.CharField(blank=True, choices=[('single', 'Célibataire'), ('married', 'Marié(e)'), ('divorced', 'Divorcé(e)'), ('widowed', 'Veuf/Veuve')], max_length=10, null=True, verbose_name='Situation Familiale')),
                ('adresse', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Adresse')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('diplome_id', models.IntegerField(blank=True, null=True, verbose_name='ID du Diplôme')),
                ('specialite', models.CharField(blank=True, max_length=100, null=True, verbose_name='Spécialité')),
            ],
            options={
                'db_table': 'candidat',
            },
        ),
        migrations.CreateModel(
            name='HRJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom du poste')),
                ('description', models.TextField(verbose_name='Description du poste')),
                ('requirements', models.TextField(verbose_name='Exigences du poste')),
                ('department', models.CharField(max_length=255, verbose_name='Département')),
                ('active', models.BooleanField(default=True, verbose_name='Actif')),
            ],
            options={
                'db_table': 'hr_job',
            },
        ),
        migrations.CreateModel(
            name='Recrutement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Description')),
                ('annonce_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Annonce')),
                ('motif', models.CharField(blank=True, choices=[('interne', 'Recrutement interne'), ('temp', 'Remplacement temporaire'), ('retr', 'Retraite')], max_length=10, null=True, verbose_name='Motif de recrutement')),
                ('pourex', models.IntegerField(default=2024, verbose_name="Pour l'exercice")),
                ('intitule', models.CharField(max_length=100, verbose_name='Intitulé du poste')),
                ('budget', models.FloatField(verbose_name='Budget')),
                ('echeanceContrat', models.DateField(blank=True, null=True, verbose_name='Échéance du contrat')),
                ('xp', models.IntegerField(verbose_name="Années d'expérience")),
                ('lieu', models.CharField(max_length=100, verbose_name='Lieu de travail')),
                ('Deplacement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Déplacement à prévoir')),
                ('autre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autres aspects à considérer')),
                ('dateEntree', models.DateField(blank=True, null=True, verbose_name="Date d'entrée")),
            ],
            options={
                'db_table': 'sirh_besoin',
            },
        ),
    ]
