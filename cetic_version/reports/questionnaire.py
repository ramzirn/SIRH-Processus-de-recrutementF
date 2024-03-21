from odoo import models


class HrApplicantReport(models.AbstractModel):
    _name = 'report.cetic_version.hr_applicant_report_template'

    def get_report_values(self, docids, data=None):
        applicants = self.env['hr.applicant'].browse(docids)
        return {
            'applicants': applicants,
        }
