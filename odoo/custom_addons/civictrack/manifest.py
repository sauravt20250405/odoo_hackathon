{
    'name': 'CivicTrack',
    'version': '1.0',
    'summary': 'Report and manage civic issues',
    'category': 'Public Services',
    'author': 'Your Team Name',
    'depends': ['base', 'mail', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/civic_issue_views.xml',
        'views/civic_issue_menus.xml',
    ],
    'application': True,
}
