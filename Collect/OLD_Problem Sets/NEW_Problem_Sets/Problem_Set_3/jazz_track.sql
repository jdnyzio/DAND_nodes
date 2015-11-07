SELECT count(DISTINCT Email)
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = "Jazz";






JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId

SELECT FirstName, LastName, BillingCity, BillingState, BillingCountry, Total
FROM Invoice JOIN Customer
(SELECT avg(Total) AS average FROM Invoice) as subquery
WHERE Total > average;


SELECT Genre.Name, COUNT(Genre.Name)
FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId,
(SELECT avg(Milliseconds) AS average FROM Track) as subquery
WHERE Milliseconds > average
GROUP BY Genre.Name
ORDER BY COUNT(Genre.Name)
DESC;
