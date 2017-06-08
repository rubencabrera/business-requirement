# -*- coding: utf-8 -*-
# © 2017 Praxya (https://www.praxya.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Business Requirement from Support',
    'category': 'Business Requirements Management',
    'summary': 'Generate Business Requirements from issues',
    'version': '8.0.1.0.0',
    'website': 'https://www.praxya.com/',
    "author": "Rubén Cabrera Martínez",
    'depends': [
        'business_requirement_deliverable_project',
        'project_issue',
    ],
    'data': [
        'wizard/br_from_issue_view.xml',
        'views/project_issue.xml',
    ],
    'image': [
        'static/description/icon.png'
    ],
    'license': 'AGPL-3',
    'installable': True,
}
