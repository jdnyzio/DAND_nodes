WORKING WITH CSV’s in SQLite
============================

To get a table from one database into only takes a few steps.

You’ll need to do the following.

-   [*EXPORT DATA TO CSV FROM DATABASE*](#export-data-to-csv-from-database)

-   [*CREATE A NEW DATABASE*](#create-a-new-database)

-   [*IMPORT YOUR CSV INTO A TABLE*](#import-your-csv-into-a-table)

You can do this with any table or query in your database.

You’ll be exporting the view you made and putting it into a new
database!

This is a useful skill but isn’t something you’ve been taught, or is
obvious without having done before. You can follow the steps below to
complete these tasks as you need them.

EXPORT DATA TO CSV FROM DATABASE
================================
```
sqlite> .mode csv

sqlite> .separator ','

sqlite> .output \<newFile.csv\>

sqlite> SELECT \* FROM \<table\>;

sqlite> .exit
```

CREATE A NEW DATABASE
=====================
```
$ sqlite3 newDB.db
```
IMPORT YOUR CSV INTO A TABLE
============================
```
sqlite> CREATE TABLE myTable()

sqlite> .mode csv

sqlite> .separator ','

sqlite> .import \<newFile\> \<myTable\>

sqlite> SELECT \* FROM \<myTable\>;
```