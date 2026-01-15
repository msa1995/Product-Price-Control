from odoo import models
from odoo.exceptions import ValidationError


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    def _check_price_limits(self):
        """
        Check min/max sale price for POS order lines.
        Safe for POS session, no JS crashes.
        """
        for line in self:
            product = line.product_id.product_tmpl_id
            price = line.price_unit

            if product.min_sale_price and price < product.min_sale_price:
                raise ValidationError(
                    f"POS Error: '{product.name}' price below minimum "
                    f"{product.min_sale_price}."
                )

            if product.max_sale_price and price > product.max_sale_price:
                raise ValidationError(
                    f"POS Error: '{product.name}' price above maximum "
                    f"{product.max_sale_price}."
                )

    def create(self, vals_list):
        """
        Override create to validate prices safely.
        """
        records = super().create(vals_list)
        records._check_price_limits()
        return records
