from odoo import models,fields

class Todo(models.Model):
    _name="aeronautica.militar"

    name=fields.Char("Modelo")
    state=fields.Selection(selection=[("bombardero","Bombardero"),("repostaje","Repostaje"),("caza","Caza"),("eletronica","Guerra electronica"),("radar","Radar"),("tropas","Transporte de tropas"),("medevac","Medevac"),("carga","Carga"),("sar","Sar"),("vigilancia","Vigilancia")])