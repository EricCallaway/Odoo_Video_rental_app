from odoo import models, fields, api


class past_due(models.TransientModel):
    _name = 'past_due'

    movie_id = fields.Many2one(string="Past due movie", comodel_name="movie")
    reason = fields.Selection(String="Reason", selection=[('damaged', 'Damaged'),
                                                                ('lost','Lost'),
                                                                ('unknown', 'Unknown')],
                                                                default="unknown")  