Modulo Profilatura di un Negozio Generico Vampi
===============================================

modulo aggiunge funzionalita ed installa i moduli necessari per il corretto funzionamento del negozio Vampigroup

Configurazione Odoo
-------------------

Abilita per l'Administrator "Funzionalità tecniche"

    Settings/Users/Users/Administrator/Usability/Technical Features

Impostazione dei dati aziendali
-------------------------------

Settings/Companies/Companies/Your Company
Rinomina Your Company in nome dell'azienda del cliente

- Imposta Accesso al Django:
    Settings/Companies/Companies/<COMPANY>/Configuration
    Compilare sezione Django
- Imposta l'immagine dell'azienda (Comparirà in alto a sinistra)

- Imposta formato indirizzo:
    Sales/Configuration/Address Book/Localization/Countries -> Italy
    Mettere ZIP davanti al city ed aggiungere i parentesi intorno al state_code:
    %(zip)s %(city)s (%(state_code)s)

- Imposta Euro prima del numero:
    Accounting/Configuration/Miscellaneous/Currencies -> EUR
    Modificare Symbol position e mettere "Before Amount"

- Imposta Bank Journal default credit and debit accounts:
    Accounting/Configuration/Journals/Journals
