# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import api, fields, models


class IcmsBook(models.TransientModel):
    _name = 'wizard.icms_book'

    date_start = fields.Date(string="Date Start")
    date_end = fields.Date(string="Date End")

    def get_report(self):
        data = {
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
            },
        }

        return self.env.ref('ax4b_fiscal.report_id').report_action(self, data=data)
