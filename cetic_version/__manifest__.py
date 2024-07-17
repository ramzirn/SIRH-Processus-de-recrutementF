# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SIRH: Processus de recrutement',
    'version': '1.0',
    'category': 'Human Ressources',
    'description': """
This module streamlines the recruitment process by managing job postings, candidate applications, and interview scheduling. It offers tools for tracking and evaluating candidates, facilitating a seamless hiring workflow.
""",
    'depends': [
        'base',
        'hr',
        'hr_recruitment',
    ],
    'data': [
        'views/besoin.xml',
        'views/candidature.xml',
        'reports/reports.xml',
        'reports/demande_de_pourvoi_de_poste.xml',
        'reports/questionnaire.xml',
        'reports/fiche_pre_selection.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
