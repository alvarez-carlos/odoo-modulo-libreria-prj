import string
from odoo import models, fields, api


class Libro(models.Model):
    _name = 'libro'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Nombre del Libro', required=True, tracking=True)
    editorial = fields.Char(string='Editorial', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    autor_id = fields.Many2one(
        comodel_name='autor', string='Autor', required=True)
    autor_apellido = fields.Char(related='autor_id.apellido', string='Apellido del Autor')
    image = fields.Binary(string='Imagen')
    categoria_id = fields.Many2one(comodel_name='categoria')
    state = fields.Selection([('borrador', 'Borrador'), ('publicado',
                             'Publicado'), ('vendido', 'Vendido')], default='borrador')
    descripcion = fields.Char(string='Descripción', compute="_compute_description")


    # sql constraints
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre del libro ya existe!'),
    ]
    # Nombre del SQL Constraint
    # unique() recibe la funcion unique y le pasamos a esta funcion las propiedades que no queremos que se dupliquen
    # Finalmente le pasamos un mensaje de error


    def boton_borrador(self):   
        # print('Has dado Click')
        self.state = 'borrador'


    def boton_publicar(self):
        # print('Has dado Click')
        self.state = 'publicado'

    def boton_vender(self):
        # print('Has dado Click')
        self.state = 'vendido'

    @api.depends('name', 'isbn')
    def _compute_description(self):
        self.descripcion = self.name + ' | '+ self.isbn




class Categoria(models.Model):
    _name = 'categoria'

    name = fields.Char(string='Nombre de la Categoria')