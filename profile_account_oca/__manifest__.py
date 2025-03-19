#
# Copyright 2016-25 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Accounting Profile",
    "version": "12.0.1.0.0",
    "category": "Technical Settings",
    "summary": "Accounting installation profile OCA",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "account",
        # "account_banking_common",                           # Only 12.0
        # "account_accountant",                               # Only 10.0
        "account_cancel",
        # "account_payment_delete",                           # Only 12.0
        # "account_group",                                    # Only 10.0
        # "l10n_it_vat_statement",
        # "account_duedates",                                 # Only 12.0
        "account_financial_report",
        "account_fiscal_year",
        # "account_invoice_constraint_chronology_nodraft",    # Only 12.0
        # "account_invoice_check_total",                      # Only 10.0
        "account_invoice_force_number",
        # "account_invoice_zero_amount",                      # Only 12.0
        "account_tax_balance",
        # "account_move_line_type",                           # Only 12.0,
        "account_move_template",
        # "account_payment_term_plus",                        # Only 12.0
        # "accounting_pdf_reports",                           # Only 12.0
        # "account_tax_unique",                               # Only 12.0
        "date_range",                                  # Only 12.0
        # "l10n_eu_account",
        # "l10n_it_account_balance_report",                   # Only 12.0
        # "l10n_it_balance",                                  # Only 12.0
        "l10n_it_central_journal",
        "l10n_it_dichiarazione_intento",
        "l10n_it_fiscalcode",
        "l10n_it_invoices_data_communication",              # Only 12.0
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
