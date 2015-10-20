#At the heart of SQL is the ability to translate your curiosity and questions into a language that a database can understand.

#The following lessons will teach you more about building your own queries and you'll find that they closely 
#resemble the way you may have originally asked the question in your native language.

#See if you can translate the following queries into the questions they were meant to answer. 

#You can also run these queries in the browser or in the local environment you've set up to see if they return what you expected!

#Example
#What songs in this dataset were written by Van Halen?
SELECT Name FROM Track WHERE Composer='Van Halen';

#Track

SELECT Name FROM Track WHERE Composer="AC/DC"; 

SELECT Composer, COUNT(*) FROM Track WHERE Composer='Queen';

SELECT Composer, SUM(Milliseconds), SUM(Bytes) FROM Track WHERE Composer='Miles Davis';

#Invoice 

SELECT min(Total), max(Total), avg(Total) from Invoice WHERE BillingCountry='Germany';

SELECT InvoiceId, BillingCity FROM Invoice WHERE BillingCountry='France';

SELECT Name, Composer, Milliseconds FROM Track WHERE Milliseconds > 4000000;

