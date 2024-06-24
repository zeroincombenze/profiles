Modulo con impostazioni base.

Sono installati i seguenti moduli:

.. $if branch in '12.0'
* remove_odoo_enterprise (rimozione link per Odoo Enterprise)
* disable_odoo_online (riferimenti odoo.com)
* portal_odoo_debranding (debranding Odoo su portale)
.. $fi
* l10n_it (Piano dei conti OCA)
* l10n_it_fiscalcode
* purchase (acquisti)
* purchase_discount (sconti su acquisti)
* report_xlsx (esportazione file Excel)
.. $if branch in '12.0'
* repository_check (aggiornamenti repository)
.. $fi
* sale (vendite)
.. $if branch in '12.0'
* sale_management (gestione vendite)
.. $fi
* stock (magazzino)
