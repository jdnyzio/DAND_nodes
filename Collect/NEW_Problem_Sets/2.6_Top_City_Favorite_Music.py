##  Now to throw an event, we need to know what kind of music they like in Prague!  
##  Can you figure out what types of music are selling the best?


---------------------BEFORE QUERY-------------------------

'''

* Write a query that returns the BillingCity and Genre Name.  

* Also create a row that shows the total number of invoices associated 
with a particular music genre.  

* Return the top 3 most popular music genres for the city you found 
using your last query.

'''
---------------------QUERY----------------------------------

QUERY ='''
SELECT Invoice.BillingCity, Genre.Name, COUNT(Genre.Name)
FROM Invoice
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE BillingCity = "Prague"
GROUP BY Genre.Name
ORDER BY COUNT(Genre.Name)
DESC
LIMIT 3;
'''
