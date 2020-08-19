from odoo import models, fields

class movie(models.Model):
    _name = 'movie'
    _rec_name = 'movie_title' #Helps with the Many2one and One2many


    movie_title = fields.Char('Title', required = True) #Title can be anything
    movie_genre = fields.Selection(string="Genre", selection=[('scifi', 'Sci-Fi'),
                                                              ('action', 'Action'),
                                                              ('horror', 'Horror'),
                                                              ('love', 'Love'),
                                                              ('comedy','Comedy')], 
                                                               default="action") 

                                                            
    movie_status = fields.Selection(String="Status", selection=[('in_stock', 'In-Stock'),
                                                                ('checked_out','Checked Out')],
                                                                default="in_stock")                    
                        
                        
    movie_num_copies = fields.Integer('Copies available', required = True)# How many copies that are available 
    movie_availability = fields.Boolean('Is the title available?', required = True) #Is the title available or not

    additional_content = fields.Many2one(string="Corresponding Video Games", comodel_name="video_games") 
    video_game_list = fields.One2many(string="Video Game List", inverse_name="additional_movie_content", comodel_name="video_games")    #Keep getting the "Uncaught TypeError: Renderer is not a constructor" error when I include this into the form view                                