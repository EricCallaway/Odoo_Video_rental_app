from odoo import models, fields

class video_games(models.Model):
    _name = 'video_games'
    _rec_name = 'game_title'

    game_title = fields.Char('Title', required = True) #Title can be anything
    game_genre = fields.Char('Genre', required = True) # Figure out how to make the genre selection only a few options i.e Horror, action, comdedy, etc...  
    ESRB_rating = fields.Char('ESRB rating', required = True)#ERSB rating
    game_num_copies = fields.Integer('copies available', required = True)# How many copies that are available 
    game_available = fields.Boolean('Is the title available?', required = True) #Is the title available or not

    additional_movie_content = fields.Many2one("movie", string="Corresponding Movies")
    
    game_status = fields.Selection(String="Status", selection=[('in_stock', 'In-Stock'),
                                                                ('checked_out','Checked Out')],
                                                                default="in_stock")         