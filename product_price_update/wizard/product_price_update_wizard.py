# -*- coding: utf-8 -*-

from odoo import api, exceptions, models, fields


class ProductPriceUpdateWizard(models.TransientModel):
    _name = 'product.price.update.wizard'

    dollar_exchange = fields.Float(string="Tasa de dólar (Bs.S)")
    product_ids = fields.Many2many('product.product', string="Productos")

    # supplier_id = fields.Many2one(
    #     'res.partner',
    #     domain=[('supplier', '=', 'True')]
    # )
    #
    #
    @api.model
    def default_get(self, fields_list):
        res = super(ProductPriceUpdateWizard, self).default_get(fields_list)
        act_ids = self._context.get("active_ids")
        # line_ids = self.env['purchase.order.line'].browse(act_ids)
        res.update({
            'product_ids': [(6, 0, act_ids)]
        })
        h = ""
        return res

    def update_price(self):
        if self.product_ids and self.dollar_exchange:
            products = self.env['product.product'].browse(self.product_ids)
            # for product in products:
            #     product.write('')

            #Crear pedido de compra
    #         order_id = self.env['purchase.order'].create({
    #             'partner_id': self.supplier_id.id
    #         })
    #
            self.product_ids.write({'list_price': 1*self.dollar_exchange})
    #
            action = self.env.ref("product.product_kanban_view").read()[0]
            action.update({
                'domain': [('id', 'in', [products[0].id])]
            })
            h=""
            return action
