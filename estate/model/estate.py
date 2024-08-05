from datetime import timedelta

from odoo import models, fields


class Estate(models.Model):
    _name = "estate"
    name = fields.Char("Title")
    description = fields.Text("Description")
    postcode = fields.Char("Post Code")
    date_availability = fields.Date("Available From", default=fields.Date.today() + timedelta(days=92), copy=False)
    expected_price = fields.Float("Expected Price")
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default="2")
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')])
    active = fields.Boolean('Active')
    state = fields.Selection(
        string="State",
        selection=[('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')], required = True, copy = False, default = "new")
    garden_area = fields.Integer("Garden Area")
