from odoo import models, fields

class CivicIssue(models.Model):
    _name = 'civic.issue'
    _description = 'Civic Issue'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    category = fields.Selection([
        ('road', 'Road'),
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('waste', 'Waste'),
        ('other', 'Other'),
    ], string='Category', required=True)
    location = fields.Char(string='Location')
    image = fields.Binary(string='Photo')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ], string='Status', default='new', tracking=True)
    reporter_id = fields.Many2one('res.partner', string='Reported By', tracking=True)
