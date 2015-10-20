**Welcome to your SQLite Environment!**
------------------------------------------

> [*Introduction*](#introduction)
>
> [*Accessing your Database*](#accessing-your-database)
>
> [*Getting Help*](#getting-help)
>
> [*Looking at Tables*](#looking-at-tables) 
>
> [*Querying Tables?*](#querying-tables)
>
> [*Finding the schema*](#finding-the-schema)
>
> [*Leaving the Database*](#leaving-the-database)

--------------------------------------------

**Introduction**
--------------------

Welcome to your SQLite environment!  Here we'll be doing the following...
* Navigating through your new workspace 
* Getting started using your first local database.
* Learning a few basic commands and running some local queries.

We'll going to take a look at the Chinook database which you can get from the Downloadables section of this course.

The Chinook database represents a digital media store, including tables for 
* artists 
* albums 
* media tracks 
* invoices  
* customers.  

You'll be getting very familiar with this database as we continue through the course. 

Let's get started!

**Accessing your Database**
--------------------

You're able to access the sqlite3 using your terminal window.

First, you need to navigate your terminal into the folder you've downloaded.

```
$ cd your/file/path/class_db
$ ls

TODO-LIST FOLDER ITEMS HERE
```

The following command will log into the Chinook_Sqlite database.
```
$ sqlite3 Chinook_Sqlite.sqlite
```
Welcome to the database!

**Getting Help**
--------------------
You can use the help command at any time to find details about all your new database superpowers.

```
sqlite> .help
```

**Looking at tables**
--------------------

Do you see these tables in your database?
```
sqlite> .tables

Album          Employee       InvoiceLine    PlaylistTrack
Artist         Genre          MediaType      Track        
Customer       Invoice        Playlist   
```

**Querying Tables**
--------------------
Let's have a look at all the data from the Invoice table.
```
sqlite> SELECT * FROM Invoice;
```
Your first query, AWESOME!

How about the Employee table?
```
sqlite> SELECT * FROM Employee;
```

You nailed it!

**Finding the schema**
--------------------
You can also look at the schema of each table using the .schema command.

```
sqlite> .schema Album
```

If you don't specify a table the .schema command will return the schema for all tables in the database.  
Take some time to explore it all!  

**Leaving the Database**
--------------------

When you're all done exploring you can leave the database.
```
sqlite> .exit 
```

Can we query the table from outside the database?
```
$ SELECT * FROM Album;
```
No you can't! Great question though.  Stay curious!

You can log back into the Chinook database to complete the problem set.

