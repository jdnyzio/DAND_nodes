sqlite> .exit
$ sqlite3 over_avg_invoice.db

sqlite> CREATE TABLE over_avg_invoice(FirstName TEXT, LastName TEXT, BillingCity TEXT, BillingState TEXT, BillingCountry TEXT, InvoiceTotal REAL);
sqlite> .tables
over_avg_invoice

sqlite> .mode csv 
sqlite> .separator ','
sqlite> .import over_avg_invoice.csv over_avg_invoice
sqlite> SELECT * FROM over_avg_invoice






