from odoo import api, fields, models


class CallCard(models.Model):
    _name = 'call.card'
    _description = 'call.card'

    code = fields.Char(string='Số phiếu mượn')
    reader_id = fields.Many2one('res.partner', string='Tên độc giả')
    reader_code = fields.Char(string='Mã độc giả')
    start_date = fields.Date(string='Ngày mượn sách')
    end_date = fields.Date(string='Ngày trả sách', default=fields.Date.today())
    due_date = fields.Date(string='Ngày đáo hạn')
    manager_id = fields.Many2one('hr.employee', string='Người xác nhận')
    description = fields.Text(string='Ghi chú mượn')
    return_note = fields.Text(string='Ghi chú trả')
    line_ids = fields.One2many('call.card.details', 'card_id', string='Chi tiết mượn')


class CallCardDetails(models.Model):
    _name = 'call.card.details'
    _description = 'call.card.details'

    card_id = fields.Many2one('call.card', string='ID phiếu mượn sách')
    book_id = fields.Many2one('product.template', string='Tên sách')
    book_code = fields.Char(string='Mã sách', related='book_id.default_code')
    publishing_company = fields.Char(string='Nhà xuất bản', related='book_id.publishing_company')
    description = fields.Text(string='Ghi chú')
