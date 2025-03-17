# -*- coding: utf-8 -*-
#
# Copyright 2016-25 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "E-Invoice Profile Zeroincombenze",
    "version": "10.0.12.0.0.1.1",
    "category": "Technical Settings",
    "summary": "E-Invoicing modules installation profile Zeroincombenze(R)",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "account",
        "l10n_it_ade",
        # "l10n_it_causali_pagamento"
        # "l10n_it_account_tax_kind"                      # Only 12.0
        # "l10n_it_fiscal_document_type_improved"         # Only 12.0
        # "l10n_it_codici_carica"                         # Only 12.0
        "l10n_it_einvoice_export_zip",
        "l10n_it_einvoice_base",
        "l10n_it_einvoice_in",
        "l10n_it_einvoice_out",
        "l10n_it_einvoice_out_li",
        "l10n_it_einvoice_out_rc",
        "l10n_it_einvoice_out_ddt",
        "l10n_it_einvoice_stamp",
        "l10n_it_einvoice_send2sdi",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
