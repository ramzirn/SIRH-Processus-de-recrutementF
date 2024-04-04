# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SIRH: Job Agency',
    'version': '1.0',
    'category': 'Human Ressources',
    'description': """
This module helps to configure the system at the installation of a new database.
ggggggggggggggggggggggggggggggggggggggggggggggggggShows you a list of applications features to install from.
    """,
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
    ],
    'data': [
        'views/recrutement.xml',
        'views/description.xml',
        'views/annonce.xml',
        'views/candidat.xml',
        'views/FicheCandidat.xml',
        'views/modifcandidatures.xml',
        'views/grilleCandidature.xml',
        'views/VueListeeCandidats.xml',
        'reports/reports.xml',
        'reports/fiche_pre_selection.xml',
        'reports/questionnaire.xml',
        'reports/demande_de_pourvoi_de_poste.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}