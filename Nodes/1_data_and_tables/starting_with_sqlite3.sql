#Navigate to the class_db folder
cd ../class_db
#Look at the databases
ls
#Go into the animals database
sqlite3 animals.db
#Check out tables
.tables
#Look at the animals table
SELECT * FROM animals;
#Make it a little prettier
.header on #show header
.mode column #break into columns
#Let's look again
SELECT * FROM animals;
#What about the other tables?
.tables
SELECT * FROM diet;

#Getting to a New database
.exit 
ls 
#Let's look at mooseball
sqlite3 mooseball.db
.tables
SELECT * FROM players;

#This is how you'll be able to access the databases locally.  You can also do many of the exercises in the browser.  Having a local setup will be important when you go off on your own so try each of the exercises this way whenever you can.