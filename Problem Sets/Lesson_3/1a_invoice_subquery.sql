#In this problem set, you'll be investigating your best customers.  
#Who are they, where are they from, and what are they spending?
#You'll use subqueries, joins, csvs, and your ability to create databases and tables to make it happen.

#For this problem, create a query that shows the city, stat, country, and total of customers whose 
#invoice totals are above the average invoice total.

SELECT BillingCity, BillingState,  BillingCountry, Total 
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;