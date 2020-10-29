# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _
from odoo.exceptions import UserError
from odoo.http import request

class AccountChartTemplate(models.Model):

    _inherit = 'account.chart.template'

    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):

        #
        # Esto deberia impedir que se creen los journals, pero no
        #

        res = super()._prepare_all_journals(acc_template_ref, company, journals_dict=journals_dict)
        if company.country_id == self.env.ref('base.ar'):
            for vals in res:
                res.remove(vals)
        return res

    @api.model
    def _get_ar_responsibility_match(self, chart_template_id):
        #
        # Machea la responsabilidad con el plan contable que es el de migracion

        """ return responsibility type that match with the given chart_template_id
        """
        match = {
#            self.env.ref('etl_companion.l10nar_base_chart_template').id: self.env.ref('l10n_ar.res_RM'),
#            self.env.ref('etl_companion.l10nar_ex_chart_template').id: self.env.ref('l10n_ar.res_IVAE'),
            self.env.ref('etl_companion.l10nar_ri_chart_template').id: self.env.ref('l10n_ar.res_IVARI'),
        }
        return match.get(chart_template_id)
