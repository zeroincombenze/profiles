# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    "name": "profile common",
    "version": "10.0.0.1.2",
    "category": "Technical Settings",
    "summary": "Common setup for all profiles",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "LGPL-3",
    "depends": [
        "account",
        # "account_banking_common",                           # Only 12.0
        "account_cancel",
        # "account_duedates",                                 # Only 12.0
        "account_financial_report",
        "account_fiscal_year",
        # "account_invoice_constraint_chronology_nodraft",    # Only 12.0
        "account_invoice_force_number",
        # "account_invoice_zero_amount",                      # Only 12.0
        # "account_move_line_type",                           # Only 12.0
        "account_move_template",
        "account_payment_term_extension",
        # "account_tax_unique",                               # Only 12.0
        "date_range",                                         # Only 12.0
        # "l10n_eu_account",
        # "l10n_it_balance",                                  # Only 12.0
        # "l10n_it_mastrini",                                 # Only 12.0
        # "l10n_it_menu",                                     # Only 12.0
        # "l10n_it_validations",                              # Only 12.0
        "l10n_it_vat_registries",
        # "l10n_it_vat_statement",                            # Only 12.0
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
