# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SIRH: Processus de recrutement',
    'version': '1.0',
    'category': 'Human Ressources',
    'description': """
This module helps to configure the system at the installation of a new database.
================================================================================

Shows you a list of applications features to install from.
    """,
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
    ],
    'data': [
        'views/formrecruitment.xml',
        'views/description_poste_views.xml',
        'views/Annonce.xml',
        'views/FicheCandidat.xml',
        'views/modifcandidatures.xml',
        'views/grilleCandidature.xml',
        'views/Annonce.xml',
        'views/FicheCandidat.xml',
        'views/modifcandidatures.xml',
        'reports/reports.xml',
        'reports/rapport_candid.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}