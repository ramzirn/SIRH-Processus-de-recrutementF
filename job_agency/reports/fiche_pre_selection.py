from odoo import models


class CandidatureReport(models.AbstractModel):
    _name = 'report.cetic_version.fiche_pre_selection_temp'

    def get_report_values(self, docids, data=None):
        var1 = self.env['sirh.candidat'].browse(docids[0])

        report_data = {
            'di': var1,
        }

        return report_data
