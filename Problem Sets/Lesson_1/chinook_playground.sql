#At the heart of any SQL query is the ability to translate your
#thoughts into a language that the database can understand.

#As you learn to build queries, you'll find that the language 
#closely resembles the structure of the question as you had 
#originally thought of it in your own languge.

#See if you can translate the following queries into the questions 
#they were meant to answer. 

#Try running these queries in the browser or in the local environment you've 
#set up to see if they return what you expected!


#QUESTION: What songs in this dataset were written by Van Halen?
SELECT Name FROM Track WHERE Composer='Van Halen';

#QUESTION:
SELECT Name FROM Track WHERE Composer="AC/DC"; 

#QUESTION:
SELECT Composer, COUNT(*) FROM Track WHERE Composer='Queen';

#QUESTION:
SELECT Composer, SUM(Milliseconds), SUM(Bytes) FROM Track WHERE Composer='Miles Davis';

#QUESTION:
SELECT min(Total), max(Total), avg(Total) from Invoice WHERE BillingCountry='Germany';

#QUESTION:
SELECT InvoiceId, BillingCity FROM Invoice WHERE BillingCountry='France';

#QUESTION:
SELECT Name, Composer, Milliseconds FROM Track WHERE Milliseconds > 4000000;

