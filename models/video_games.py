from odoo import models, fields

class video_games(models.Model):
    _name = 'video_games'

    game_title = fields.Char('Title', required = True) #Title can be anything
    game_genre = fields.Char('Genre', required = True) # Figure out how to make the genre selection only a few options i.e Horror, action, comdedy, etc...  
    ERSB_rating = fields.Char('ERSB rating', required = True)#ERSB rating
    num_copies = fields.Integer('Copies available', required = True)# How many copies that are available 
    available = fields.Boolean('Is the title available?', required = True) #Is the title available or not
                                         