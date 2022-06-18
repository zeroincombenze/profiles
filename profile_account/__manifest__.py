# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "profile account",
    "version": "10.0.0.1.2",
    "category": "Technical Settings",
    "summary": "Accounting installation profile",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "account",
        "account_accountant",                               # Only 10.0
        # "account_banking_common",                           # Only 12.0
        "account_cancel",
        # "account_cancel_payment",                           # Only 12.0
        "account_vat_period_end_statement",
        # "account_duedates",                                 # Only 12.0
        # TODO> Strange error!
        # "account_financial_report",
        "account_fiscal_year",
        # "account_invoice_constraint_chronology_nodraft",    # Only 12.0
        "account_invoice_check_total",
        "account_invoice_force_number",
        # "account_invoice_zero_amount",                      # Only 12.0
        # "account_move_line_type",                           # Only 12.0
        "account_move_template",
        "account_payment_term_extension",
        # "account_tax_unique",                               # Only 12.0
        "date_range",                                         # Only 12.0
        # "l10n_eu_account",
        # "l10n_it_balance",                                  # Only 12.0
        "l10n_it_central_journal",
        "l10n_it_einvoice_export_zip",
        "l10n_it_einvoice_in",
        "l10n_it_einvoice_out",
        "l10n_it_einvoice_out_li",
        "l10n_it_fiscalcode",
        "l10n_it_lettera_intento",
        # "l10n_it_mastrini",                                 # Only 12.0
        # "l10n_it_menu",                                     # Only 12.0
        "l10n_it_reverse_charge",
        "l10n_it_split_payment",
        # "l10n_it_validations",                              # Only 12.0
        "l10n_it_vat_communication",
        "l10n_it_vat_registries",
        # "l10n_it_vat_statement",                            # Only 12.0
        "l10n_it_vat_statement_communication",
        "l10n_it_withholding_tax",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
