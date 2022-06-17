Module with common setup to customize an Odoo instance.

It installs:
Personalizzazione

Modulo con impostazioni base per installazione Odoo.

Sono installati i seguenti moduli:

* base
.. $if branch in '12.0'
* remove_odoo_enterprise
* disable_odoo_online
* portal_odoo_debranding
.. $fi
* l10n_it_fiscalcode
* report_xlsx
.. $if branch in '12.0'
* repository_check
.. $fi
