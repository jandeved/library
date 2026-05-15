# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBookInherit(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one('res.partner', string='Author', required=True)

    # Used category_ids instead of category_id since many2many relationship is used
    category_ids = fields.Many2many('library.book.category', string='Book Categories')