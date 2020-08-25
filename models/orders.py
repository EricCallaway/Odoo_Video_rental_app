from odoo import models, fields

class orders(models.Model):
    _name = 'orders'
    _rec_name = 'movie_order'


    

    
                                                            
    movie_order = fields.Many2one("movie", string="Movie ordered") 
    game_order = fields.Many2one("video_games", string="Video Game ordered")
    date_of_order = fields.Date(string="Date of Order")
    

