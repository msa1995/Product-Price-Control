{
    "name": "Product Min/Max Sale Price Control",
    "version": "1.0",
    "category": "Sales",
    "author": "Muhannad Saleh",
    "summary": "Control minimum and maximum sale prices for products",
    "description": """
    Adds minimum and maximum sale price control.
    Prevents sales and POS orders outside allowed price range.
    """,
    "depends": [
        "product",
        "sale_management",
        "point_of_sale",
        "pos_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_view.xml",
    ],
    "installable": True,
    "application": False,
}
