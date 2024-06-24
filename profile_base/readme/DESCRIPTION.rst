Module with common setup to customize.

It installs:

.. $if branch in '12.0'
* remove_odoo_enterprise
* disable_odoo_online
* portal_odoo_debranding
.. $fi
* l10n_it_coa (Chart of Account Zeroincombenze)
* l10n_it_fiscalcode
* purchase
* purchase_discount
* report_xlsx
.. $if branch in '12.0'
* repository_check
.. $fi
* sale
.. $if branch in '12.0'
* sale_management
.. $fi
* stock
