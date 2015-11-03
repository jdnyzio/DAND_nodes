sqlite> .mode list
sqlite> .separator , 
sqlite> .output over_avg_ms.csv
sqlite> SELECT * FROM over_avg_ms;
sqlite> .exit


$ sqlite3 view.db

sqlite> CREATE TABLE over_avg_ms(Composer TEXT, Song TEXT, Genre TEXT, Milliseconds INTEGER);
sqlite> .tables
over_avg_ms
sqlite> 
