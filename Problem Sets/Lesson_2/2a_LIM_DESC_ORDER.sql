#In this problem set, you'll practice constructing queries from a given question.  

#Sometimes it's useful to break down more complex questions into smaller components.
#You can then use these smaller pieces to help piece together your query.

#QUESTION: What 5 countries have the most total invoices?  
#Your query should return the names of the countries followed by the number of invoices.

#Step 1: What are you trying to find out?
#Answer: The Number of Invoices to each BillingCountry

#Step 2: What table do you need to look at?
#ANSWER: Invoice

#Step 3: What columns will you need for the query?
#ANSWER: BillingCountry, total number of invoices

#Step 4: Do you need to do anything with this column?
#ANSWER: COUNT 

#Step 5: How should they be ordered?
#ANSWER: Total number of invoices at the top (DESC)

#Step 6: How many records do you want to see?
ANSWER: 5, LIMIT 5

#Now you can put it all together!
#Use the questions above to fill in the query structure below to build your query!

SELECT BillingCountry, COUNT(*)
FROM Invoice 
GROUP BY BillingCountry
ORDER BY COUNT(*)
DESC
LIMIT 5;