Your New Environment
=============================

After following instructions from the last slide, you're
now the proud owner of a local SQLite environment!  You are
ready to start navigating the Chinook Database which you'll be working 
with through the next few problem sets.

* Below are some important commands you can use to help explore your
new workspace.

* Type the following commands into your terminal window to get started using SQLite3.

#Accessing your database
```
cd your/file/path/class_db
ls
```

Let's log into the Chinook_Sqlite database.
```
sqlite3 Chinook_Sqlite.sqlite
```

#Finding Help
```
.help
```
Reaching out for help is a great way to learn.

What tables do you see in the database?
```
.tables

Album          Employee       InvoiceLine    PlaylistTrack
Artist         Genre          MediaType      Track        
Customer       Invoice        Playlist   
```

#Could you tell me what data is in the Invoice table?
```
SELECT * FROM Invoice;
```
Thanks for your help!

Try another table.
```
SELECT * FROM instruments;
```
Whoops, what happened!?
```
.tables
```
Looks like instruments isn't actually a table in the database.  
No harm done though.  Don't be afraid to try new things :)

Have a look at some of the other tables just how you did with the Invoice table.
```
SELECT * FROM Artist;
```

Go crazy, explore it all!

When you're all done exploring you can leave the database.
```
.exit 
```
Goodbye friend.

Can we query the table from outside the database?
```
SELECT * FROM Album;
```
No you can't! Great question though.  Stay curious!

