#
# Copyright 2018-24 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Payment profile",
    "version": "12.0.1.0.2",
    "category": "Technical Settings",
    "summary": "Payment and financial modules installation",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "assigned_bank",
        "account_banking_invoice_financing",
        "account_banking_riba",
        # "account_banking_sepa_credit_trasfer_ita",
        # "account_banking_sepa_direct_debit_ita",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
