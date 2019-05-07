# -*- coding: utf-8 -*-

from odoo import api, exceptions, models, fields


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book", default="NEW")
    description = fields.Text(string="Description")
    isbn = fields.Char(string="ISBN")

    # ===== Python constraint =====
    #Importar la libreria api y exceptions
    @api.constrains('isbn')
    def check_isbn(self):
        isbn = self.search([['id','!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError('ISBN duplicado')

    # ===== MANY TO ONE =======
    # category_id = fields.Many2one(
    #
    #     comodel_name='library.category', string="Category"
    # )

    # ====== MANY TO MANY =========
    # category_ids = fields.Many2many(
    #
    #     comodel_name='library.category', string="Categories"
    # )

    # ====== ONE TO MANY ============
    category_ids = fields.One2many(

        comodel_name='library.category', inverse_name="book_id", string="Categories"
    )

    # ========== SQL CONSTRAINT ==========
    _sql_constraints = [
        ('name_unique', 'unique (name)', """El nombre del libro debe ser único"""),
    ]
