#In this problem set, you'll be investigating your best customers.  
#Who are they, where are they from, and what are they spending?
#You'll use subqueries, joins, csvs, and your ability to create databases and tables to make it happen.

#For this problem, create a query that shows the city, stat, country, and total of customers whose 
#invoice totals are above the average invoice total.

SELECT BillingCity, 
       BillingState,  
       BillingCountry, 
       Total 
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;




#SUBQUERY 2

SELECT DISTINCT(Composer), COUNT(*)
FROM Track, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;


SELECT avg(bigscore) 
FROM (SELECT max(score) as bigscore 
      FROM mooseball 
      GROUP BY team) as maxes
      
      
SELECT Composer, avg(Bytes) 
FROM (SELECT Composer, Bytes 
      FROM Track 
      WHERE Composer='Apocalyptica');
      
      
SELECT BillingCity, 
       BillingState,  
       BillingCountry, 
       Total 
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;

      
SELECT Name, Bytes
FROM Track, 
    (SELECT avg(bytes) as average 
     FROM Track) as subquery
WHERE Bytes < average;


#SUBQUERY 3

How many invoices were receieved by the top 5 Countries?

SELECT sum(total)
FROM 
(SELECT BillingCity, COUNT(*) as total
FROM Invoice 
GROUP BY BillingCountry
ORDER BY COUNT(*)
DESC
LIMIT 5) AS subquery;