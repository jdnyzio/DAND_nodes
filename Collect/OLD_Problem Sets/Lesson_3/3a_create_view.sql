#In this problem set, you'll be investigating your best customers.  
#Who are they, where are they from, and what are they spending?
#You'll use subqueries, joins, csvs, and your ability to create databases and tables to make it happen.

#Now you'll want to create a view of your query to easily access this information.

#Here is an example of a view you've seen in class

#CREATE VIEW course_size as 
#SELECT course_id, COUNT(*) as num
#FROM enrollment
#GROUP by course_id;

#See if you can turn your query into a view!

CREATE VIEW over_avg_invoice AS
SELECT Customer.FirstName, 
       Customer.LastName, 
       Invoice.BillingCity, 
       Invoice.BillingState,  
       Invoice.BillingCountry, 
       Invoice.Total 
FROM Invoice JOIN Customer, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;
ON Customer.CustomerId=Invoice.CustomerId;







