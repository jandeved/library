# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"

    # SQL Constraint for book category uniqueness
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The book category must be unique!')
    ]

    name = fields.Char('Book Category', required=True)