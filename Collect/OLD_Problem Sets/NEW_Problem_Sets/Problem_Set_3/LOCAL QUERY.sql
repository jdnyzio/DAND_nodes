SELECT count(DISTINCT Email)
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = "Jazz";


SELECT count(MediaType.Name), Genre.Name
FROM Track
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE MediaType.Name = 'MPEG audio file'
AND Genre.Name = 'Pop';


SELECT Genre.Name, COUNT(Genre.Name)
FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId,
(SELECT avg(Milliseconds) AS average FROM Track) as subquery
WHERE Milliseconds < average
GROUP BY Genre.Name
ORDER BY COUNT(Genre.Name)
DESC
LIMIT 1;


INSERT INTO [Track] ([TrackId], [Name], [AlbumId], [MediaTypeId], [GenreId], [Composer], [Milliseconds], [Bytes], [UnitPrice]) VALUES (3504, 'Udacity Theme Song', 34, 1, 9, 'Udaciband', 230321, 3872240, 1.99);