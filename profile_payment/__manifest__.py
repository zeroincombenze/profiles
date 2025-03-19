#
# Copyright 2016-25 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Payment profile Zeroincombenze",
    "version": "12.0.1.0.2",
    "category": "Technical Settings",
    "summary": "Payment and financial modules installation Zeroincombenze(R)",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "assigned_bank",
        "account_banking_invoice_financing",
        "account_banking_riba",
        # "account_banking_sepa_credit_trasfer_ita",
        # "account_banking_sepa_direct_debit_ita",
        "l10n_it_account_stamp",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
