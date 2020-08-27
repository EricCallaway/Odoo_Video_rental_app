from odoo import models, fields, api

class Customer(models.Model):
    _inherit = 'res.partner'

    #Customer details
    customer_rating = fields.Selection(String="Customer Rating", selection=[('bad_customer', 'Bad Customer'),
                                                                   ('good_customer', 'Good Customer')],
                                                                   default='good_customer')
    #Sale details to determine the rating of the customer
    num_items_ordered = fields.Integer('Number of items rented out', required=True)
    num_late_returns = fields.Integer('Number of times that this customer has returned the rentals late.', requried=True)

    #I know of a much better way of doing this i.e set up a counter variable, but I want to just make sure I can get it working first
    #Method that determines if the customer is a good customer or not
    # @api.depends('num_late_returns')
    # def set_customer_rating(self):
       
    
    @api.multi
    def write(self, vals):
        if self.num_late_returns > 3:
            vals["customer_rating"] = 'bad_customer'
        else:
            vals["customer_rating"] = 'good_customer'
        res = super(Customer, self).write(vals)
        return res


