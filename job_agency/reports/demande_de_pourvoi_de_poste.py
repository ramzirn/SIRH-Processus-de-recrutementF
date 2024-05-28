from odoo import models


class PourvoiPosteReport(models.AbstractModel):
    _name = 'report.job_agency.dem_pourvoi_temp'

    def get_report_values(self, docids, data=None):
        var1 = self.env['sirh.besoin'].browse(docids[0])

        report_data = {
            'di': var1,
        }

        return report_data
