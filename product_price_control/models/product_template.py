from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Minimum allowed sale price
    min_sale_price = fields.Float(
        string="Minimum Sale Price",
        help="The minimum price this product can be sold for."
    )

    # Maximum allowed sale price
    max_sale_price = fields.Float(
        string="Maximum Sale Price",
        help="The maximum price this product can be sold for."
    )

    @api.constrains("min_sale_price", "max_sale_price")
    def _check_min_max_sale_price(self):
        """
        Ensure that the minimum sale price does not exceed the maximum sale price.
        """
        for product in self:
            if (
                product.min_sale_price
                and product.max_sale_price
                and product.min_sale_price > product.max_sale_price
            ):
                raise ValidationError(
                    "Minimum Sale Price cannot be greater than Maximum Sale Price."
                )
