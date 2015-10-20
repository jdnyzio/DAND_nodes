sqlite> .mode csv
sqlite> .separator ',' 
sqlite> .output over_avg_invoice.csv
sqlite> SELECT * FROM over_avg_invoice;
sqlite> .exit