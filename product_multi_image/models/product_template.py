# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3).
# © 2009 Sharoon Thomas Open Labs Business Solutions
# © 2014 Serv. Tecnol. Avanzados Pedro M. Baeza
# © 2015 Antiun Ingeniería S.L. - Jairo Llopis
# © 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = [_name, 'base_multi_image.owner']

    image = fields.Binary(related='image_main')
    image_medium = fields.Binary(related='image_main_medium')
    image_small = fields.Binary(related='image_main_small')
