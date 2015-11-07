#At the heart of any SQL query is the ability to translate your
#thoughts into a language that the database can understand.

#You'll find that SQL queries closely resemble the 
#structure of your own question as you had 
#thought of it in your own language.

#See if you can translate the following queries into the questions 
#they were meant to answer. 

#Try running these queries in the browser or in the local environment you've 
#set up to see if they return what you expected!


#QUESTION: What songs in this dataset were written by Van Halen?
SELECT Name FROM Track WHERE Composer='Van Halen';
#Another possibility: Can you find which songs Van Halen wrote that are in the dataset?

#QUESTION:What songs in this dataset were written by AC/DC?
SELECT Name FROM Track WHERE Composer="AC/DC"; 

#QUESTION: How many songs in this dataset were written by Queen?
SELECT Composer, COUNT(*) FROM Track WHERE Composer='Queen';

#QUESTION: What is the total time and file size of the songs written by Miles Davis in this dataset?
SELECT Composer, SUM(Milliseconds), SUM(Bytes) FROM Track WHERE Composer='Wolfgang Amadeus Mozart';

#QUESTION: What is the minimum, maximum, and average total bill on an invoice sent to Germany?
SELECT min(Total), max(Total), avg(Total) from Invoice WHERE BillingCountry='Germany';

#QUESTION: What are the invoice Id's and billing cities for all invoices sent to France?
SELECT InvoiceId, BillingCity FROM Invoice WHERE BillingCountry='France';

#QUESTION: What is the song title, composer, and time of each track in the dataset 
#that runs longer than 4000000 milliseconds.
SELECT Name, Composer, Milliseconds FROM Track WHERE Milliseconds > 4000000;

