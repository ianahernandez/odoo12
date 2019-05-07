# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book")
    description = fields.Text(string="Description")

    # ===== MANY TO ONE =======
    # category_id = fields.Many2one(
    #
    #     comodel_name='library.category', string="Category"
    # )

    # ====== MANY TO MANY
    # category_ids = fields.Many2many(
    #
    #     comodel_name='library.category', string="Categories"
    # )

    # ====== ONE TO MANY
    category_ids = fields.One2many(

        comodel_name='library.category', inverse_name="book_id", string="Categories"
    )
