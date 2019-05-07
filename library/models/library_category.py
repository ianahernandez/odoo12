# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryCategory(models.Model):
    _name = "library.category"

    name = fields.Char(string="Category")
    description = fields.Text(string="Description")

    # ====== ONE TO MANY (Campo relacional)
    book_id = fields.Many2one(
        comodel_name="library.book", string="Libro"
    )
