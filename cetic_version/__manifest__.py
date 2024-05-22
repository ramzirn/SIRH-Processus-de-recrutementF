# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SIRH: Processus de recrutement',
    'version': '1.0',
    'category': 'Human Ressources',
    'description': """
This module helps to configure the system at the installation of a new database.

Shows you a list of applications features to install from.
    """,
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
    ],
    'data': [
        # 'views/candidat.xml',
        # 'views/candidature.xml',
        # 'views/description.xml',
        # 'views/entretien.xml',
        'views/FicheCandidat.xml',
        'views/recrutement.xml',
        # 'views/besoin.xml',
        'views/grilleCandidat.xml',
        'views/modifcandidatures.xml',
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
