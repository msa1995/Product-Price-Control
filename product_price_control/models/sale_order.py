from odoo import models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        """
        Prevent confirmation of sales orders if any line violates
        the product's minimum or maximum sale price.
        """
        for order in self:
            for line in order.order_line:
                product = line.product_id.product_tmpl_id
                price = line.price_unit

                if product.min_sale_price and price < product.min_sale_price:
                    raise ValidationError(
                        f"Product '{product.name}' cannot be sold below "
                        f"{product.min_sale_price}."
                    )

                if product.max_sale_price and price > product.max_sale_price:
                    raise ValidationError(
                        f"Product '{product.name}' cannot be sold above "
                        f"{product.max_sale_price}."
                    )

        return super().action_confirm()
