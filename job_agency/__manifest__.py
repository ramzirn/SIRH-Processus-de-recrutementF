# -*- coding: utf-8 -*-
{
    'name': 'SIRH: Job Agency',
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
        'views/annonce.xml',
        'views/besoin.xml',
        'views/candidature.xml',
        'views/entretien.xml',
        'views/evalcandidat.xml',
        'views/poste.xml',
        'data/candi.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
# Part of Odoo. See LICENSE file for full copyright and licensing details.
