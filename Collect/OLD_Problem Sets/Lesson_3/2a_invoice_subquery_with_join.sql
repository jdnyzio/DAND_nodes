#In this problem set, you'll be investigating your best customers.  
#Who are they, where are they from, and what are they spending?
#You'll use subqueries, joins, csvs, and your ability to create databases and tables to make it happen.

#Now that you've got the city, state, country, and invoice total, you'll need to find a way to include the 
#customer's first and last name in the query.

#Here is an example of a JOIN you've seen in class.
#SELECT Album.Title, Artist.Name 
#FROM Album JOIN Artist 
#ON Artist.ArtistId = Album.ArtistId;

#See if you can add to your previous query and create a query that includes all the information you need!

#Your Query 
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







