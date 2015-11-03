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
WHERE Total > av
ORDER BY Total;

How many invoice totals are above the average total?

SELECT sum(Total)
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq
WHERE Total > av;




SELECT BillingCity, 
       BillingState,  
       BillingCountry, 
       Total 
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av
AND BillingCountry='France';

      
SELECT Name, Bytes
FROM Track, 
    (SELECT avg(bytes) as average 
     FROM Track) as subquery
WHERE Bytes < average;


#SUBQUERY 3

How many invoices were receieved by the top 5 Countries?

SELECT sum(total)
FROM (SELECT COUNT(*) as total 
      FROM Invoice 
      GROUP BY BillingCountry
      ORDER BY total
      DESC LIMIT 5);
      
      
SELECT FirstName, LastName, BillingCity, BillingState, BillingCountry, Total
FROM Invoice JOIN Customer, 
    (SELECT avg(Total) AS average
    FROM Invoice) AS subquery
WHERE Total > average;
      


CREATE TABLE [Track]
(
    [Name] NVARCHAR(200)  NOT NULL,
    [Composer] NVARCHAR(220),
    [Milliseconds] INTEGER  NOT NULL,
    [Bytes] INTEGER
);


CREATE TABLE [Track]
(
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [BillingCity] NVARCHAR(40),
    [BillingState] NVARCHAR(40),
    [BillingCountry] NVARCHAR(40),
    [Total] NUMERIC(10,2)  NOT NULL
);







