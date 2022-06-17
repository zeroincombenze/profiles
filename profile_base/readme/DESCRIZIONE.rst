Personalizzazione

Modulo con impostazioni base per installazione Odoo.

Sono installati i seguenti moduli:

* base
.. $if branch in '12.0'
* remove_odoo_enterprise (rimozione link per Odoo Enterprise)
* disable_odoo_online (riferimenti odoo.com)
* portal_odoo_debranding (debranding Odoo su portale)
.. $fi
* l10n_it_fiscalcode
* report_xlsx (esportazione file Excel)
.. $if branch in '12.0'
* repository_check (aggiornamenti repository)
.. $fi
