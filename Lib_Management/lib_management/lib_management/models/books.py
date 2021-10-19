from odoo import api, fields, models


class LibProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string='Tên đầu sách', required=True)
    publishing_company = fields.Char(string='Nhà xuất bản')
    is_book = fields.Boolean(string='Is Book', default=False)

    @api.model
    def default_get(self, fields):
        res = super(LibProductTemplate, self).default_get(fields)
        res.update({
            'type': 'service',
            'currency_id': self.env.ref('base.VND').id,
        })
        return res
