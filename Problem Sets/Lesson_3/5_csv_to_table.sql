sqlite> .exit
$ sqlite3 over_avg_invoice.db

sqlite> .mode csv 
sqlite> .separator ','
sqlite> .import over_avg_invoice.csv over_avg_invoice
sqlite> SELECT * FROM over_avg_invoice






