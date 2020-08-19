from odoo import models, fields

class orders(models.Model):
    _name = 'orders'

    #Movie_or_Video_game = fields.Char('Movie or Video game.', required = True)
    #Movie_or_Video_game = fields.Selection(selection_add=[('Movie','Video games')], 'state', default="Movie")
    Movie_or_Video_game = fields.Selection(string="Type", selection=[('movie', 'Movie'),
                                                              ('video_game', 'Video Game')],
                                                               default="movie")