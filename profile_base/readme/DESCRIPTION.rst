Module with common setup to customize to install **after** you installed localization
module, like *l10n_it_coa* or *l10n_it*

It installs:

.. $if branch in '12.0'
* remove_odoo_enterprise
* disable_odoo_online
* portal_odoo_debranding
.. $fi
* l10n_it_fiscalcode
* purchase
* purchase_discount
* report_xlsx
.. $if branch in '12.0'
* repository_check
.. $fi
* sale
* sale_management
* stock
