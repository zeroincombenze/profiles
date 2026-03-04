# -*- coding: utf-8 -*-
#
# Copyright 2016-26 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Accounting Profile",
    "version": "10.0.1.0.2",
    "category": "Technical Settings",
    "summary": "Accounting installation profile OCA",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "account",
        "account_accountant",
        "account_cancel",
        "account_group",
        "account_vat_period_end_statement",
        "account_fiscal_year",
        "account_invoice_check_total",
        "account_invoice_force_number",
        "account_tax_balance",
        "account_move_template",
        "account_payment_term_extension",
        "date_range",
        "l10n_it_central_journal",
        "l10n_it_dichiarazione_intento",
        "l10n_it_fiscalcode",
        "l10n_it_reverse_charge",
        "l10n_it_split_payment",
        "l10n_it_vat_registries",
        "l10n_it_withholding_tax",
        "account_financial_report_qweb",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
