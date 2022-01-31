from odoo import models, fields


class Autor(models.Model):
    _name = 'autor'
    _rec_name = 'apellido'

    name = fields.Char(string='Nombre del Autor', required=True)
    apellido = fields.Char(string='Apellido del Autor', required=True)
