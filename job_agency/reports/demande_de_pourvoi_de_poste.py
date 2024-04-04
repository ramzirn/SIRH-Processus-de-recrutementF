from odoo import models


class PourvoiPosteReport(models.AbstractModel):
    _name = 'report.cetic_version.dem_pourvoi_temp'

    def get_report_values(self, docids, data=None):
        var1 = self.env['sirh.form'].browse(docids[0])

        report_data = {
            'di': var1,
        }

        return report_data
