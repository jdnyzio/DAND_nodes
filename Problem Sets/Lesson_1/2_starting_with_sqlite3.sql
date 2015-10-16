#After downloading everything from the last slide, you're
now the proud owner of a local SQLite environment!

#Here are some important commands you can use to help explore your
new toys.

#Type the following commands into your terminal window to get started using SQLite3.

#Take a peek at your new class_db folder through your terminal window.
cd your/file/path/class_db
ls

#Let's log into the Chinook_Sqlite database
sqlite3 Chinook_Sqlite.sqlite

#What tables do you see in the database?
.tables

#Could you tell me what data is in the Invoice table?
SELECT * FROM Invoice;
#Thanks so much!

#Try another table.
SELECT * FROM instruments;
#Whoops, what happened!?
.tables

#Looks like instruments isn't actually a table in the database.  
#No harm done though.  Don't be afraid to try new things :)

#Have a look at some of the other tables just how you did with the Invoice table.
SELECT * FROM tableName;
#Go crazy, explore it all!

#When you're all done exploring you can leave the database.
.exit 
#Goodbye friend.

#Can we query the table from outside the database?
SELECT * FROM Album;
#No you can't! Great question though.  Stay curious.

