from odoo import models, fields

class movie(models.Model):
    _name = 'movie'

    movie_title = fields.Char('Title', required = True) #Title can be anything
    movie_genre = fields.Selection(string="Genre", selection=[('scifi', 'Sci-Fi'),
                                                              ('action', 'Action'),
                                                              ('horror', 'Horror'),
                                                              ('love', 'Love'),
                                                              ('comedy','Comedy')], 
                                                               default="action") 
                        
                        
                        
    movie_num_copies = fields.Integer('Copies available', required = True)# How many copies that are available 
    movie_availability = fields.Boolean('Is the title available?', required = True) #Is the title available or not

    additional_content = fields.Many2one("video_games", string="Corresponding Video Games") 
    #video_game_list = fields.One2many("video_games", "additional_movie_content", string="Video Game List")
    #Keep getting the "Uncaught TypeError: Renderer is not a constructor" error when I include this into the form view                                