#After downloading SQLite3, you'll have the chance to run many of the class exercises locally.

#This will help prepare you for the skills you'll need to complete the project later on, 
#and give you confidence managing your own local environment.  Here are a few simple commands 
#to help get you started.  

#Type the following commands directly into your terminal window to get started using SQLite3.

#Navigate to the class_db folder
cd class_db
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

#These commands are a simple way to get started using your new SQLite environment.
#Try to continue experimenting locally while progressing through the course.