# -*- coding: utf-8 -*-
#
# Copyright 2016-24 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Accounting Profile",
    "version": "10.0.0.1.2",
    "category": "Technical Settings",
    "summary": "Accounting installation profile",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "account",
        # "account_banking_common",                           # Only 12.0
        "account_accountant",                               # Only 10.0
        "account_cancel",
        # "account_payment_delete",  # Only 12.0
        "account_group",                                    # Only 10.0
        "account_vat_period_end_statement",                 # Only 10.0
        # "account_duedates",                                 # Only 12.0
        # "account_financial_report",
        "account_fiscal_year",
        "account_invoice_check_total",                      # Only 10.0
        "account_invoice_force_number",
        # "account_invoice_zero_amount",                      # Only 12.0
        "account_tax_balance",
        # "account_move_line_type",                           # Only 12.0,
        "account_move_template",
        "account_payment_term_extension",
        # "account_tax_unique",                               # Only 12.0
        "date_range",
        "l10n_eu_account",
        # "l10n_it_account_balance_report",                   # Only 12.0
        # "l10n_it_balance",                                  # Only 12.0
        "l10n_it_central_journal",
        "l10n_it_lettera_intento",
        "l10n_it_fiscalcode",
        "l10n_it_vat_communication",
        # "l10n_it_mastrini",                                 # Only 12.0
        # "l10n_it_menu",                                     # Only 12.0
        "l10n_it_reverse_charge",
        "l10n_it_split_payment",
        # "l10n_it_validations",                              # Only 12.0
        "l10n_it_vat_registries",
        "l10n_it_vat_statement_communication",
        "l10n_it_withholding_tax",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
