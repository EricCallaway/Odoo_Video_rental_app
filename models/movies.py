from odoo import models, fields

class movie(models.Model):
    _name = 'movie'

    movie_title = fields.Char('Title', required = True) #Title can be anything
    movie_genre = fields.Char('Genre', required = True) # Figure out how to make the genre selection only a few options i.e Horror, action, comdedy, etc...  
    movie_num_copies = fields.Integer('Copies available', required = True)# How many copies that are available 
    movie_availability = fields.Boolean('Is the title available?', required = True) #Is the title available or not
                                         