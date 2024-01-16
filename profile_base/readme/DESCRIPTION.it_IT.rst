Modulo con impostazioni base da installare **dopo** aver installato il modulo di
localizzazione quali *l10n_it_coa* o *l10n_it*.

Sono installati i seguenti moduli:

.. $if branch in '12.0'
* remove_odoo_enterprise (rimozione link per Odoo Enterprise)
* disable_odoo_online (riferimenti odoo.com)
* portal_odoo_debranding (debranding Odoo su portale)
.. $fi
* l10n_it_fiscalcode
* purchase (acquisti)
* purchase_discount (sconti su acquisti)
* report_xlsx (esportazione file Excel)
.. $if branch in '12.0'
* repository_check (aggiornamenti repository)
.. $fi
* sale (vendite)
* sale_management (gestione vendite)
* stock (magazzino)
