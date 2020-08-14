# -*- coding: utf-8 -*-
from odoo import http

class MovieRentals(http.Controller):

    @http.route('/movie__rentals/movie__rentals/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/movie__rentals/movie__rentals/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('movie__rentals.listing', {
            'root': '/movie__rentals/movie__rentals',
            'objects': http.request.env['movie__rentals.movie__rentals'].search([]),
        })

    @http.route('/movie__rentals/movie__rentals/objects/<model("movie__rentals.movie__rentals"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('movie__rentals.object', {
            'object': obj
        })