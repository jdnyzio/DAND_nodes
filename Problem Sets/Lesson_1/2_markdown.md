Welcome to your SQLite Environment!
=============================

After following instructions from the last slide, you're
now the proud owner of a local SQLite environment.  You are
ready to start navigating your brand new workspace.

We'll start off by getting you familiar with the Chinook database which 
you'll be using throughout these problem sets to practice using SQL.

The Chinook database represents a digital media store, including 
tables for artists, albums, media tracks, invoices and customers.  

##Accessing your database

* Below are some important commands you can use to help explore your
new workspace.

* Type the following commands into your terminal window to get started using SQLite3.

```
$ cd your/file/path/class_db
$ ls
```

Let's log into the Chinook_Sqlite database.
```
$ sqlite3 Chinook_Sqlite.sqlite
```

##Finding Help
```
sqlite> .help
```
Reaching out for help is a great way to learn.

What tables do you see in the database?
```
sqlite> .tables

Album          Employee       InvoiceLine    PlaylistTrack
Artist         Genre          MediaType      Track        
Customer       Invoice        Playlist   
```

##Querying your tables
Look at all the data from the Invoice table.
```
sqlite> SELECT * FROM Invoice;
```
Try another table.
```
sqlite> SeLECt * froM EmPlOYee;
```
Did you notice that?  Capitalization doesn't matter in a SQL query!
You'll often see commands such as SELECT, FROM, and WHERE in capital letters.
This is only used to help us read it more easily but the computer doesn't care at all.

##Schema
You can also look at the schema using the .schema command.
```
sqlite> .schema Album

CREATE TABLE [Album]
(
    [AlbumId] INTEGER  NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    CONSTRAINT [PK_Album] PRIMARY KEY  ([AlbumId]),
    FOREIGN KEY ([ArtistId]) REFERENCES [Artist] ([ArtistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE UNIQUE INDEX [IPK_Album] ON [Album]([AlbumId]);
CREATE INDEX [IFK_AlbumArtistId] ON [Album] ([ArtistId]);

```
Use .help, .table, .schema look at some of the other tables.  
Go crazy, explore it all!

When you're all done exploring you can leave the database.
```
sqlite> .exit 
```

Can we query the table from outside the database?
```
$ SELECT * FROM Album;
```
No you can't! Great question though.  Stay curious!

