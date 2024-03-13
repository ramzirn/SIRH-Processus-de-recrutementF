from odoo import models, fields, api, _

class CandidatureReport(models.AbstractModel):
    _name = 'report.CETIC_version.candid'

    def get_report_values(self, docids, data=None):
        var1 = self.env['candidat'].browse(docids[0])
        print(var1)
        report_data = {
            'di': var1,
        }

        return report_data
