# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "ITA - Fiscal localization for CdO",
    "version": "12.0.1.0.0",
    "category": "Localization/Account Charts",
    "summary": "ITA - Fiscal localization by Zeroincombenze(R)",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/fatturazione-elettronica",
    "development_status": "Production/Stable",
    "license": "LGPL-3",
    "depends": [
        "account",
        "base_vat",
        "base_iban",
    ],
    "data": [
        "data/l10n_it_chart_data.xml",
        "data/account.group.csv",
        "data/account.account.template.csv",
        "data/account.tax.group.csv",
        "data/account.tax.template.csv",
        "data/account.fiscal.position.template.csv",
        "data/account.chart.template.csv",
        "data/account_chart_template_data.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
