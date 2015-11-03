

#Your Query 
SELECT Customer.FirstName, 
       Customer.LastName, 
       Invoice.BillingCity, 
       Invoice.BillingState,  
       Invoice.BillingCountry, 
       Invoice.Total 
FROM Invoice JOIN Customer, 
ON Customer.CustomerId=Invoice.CustomerId;

Get all address information onto the same tables
Invoice - Date
Customer - Email


List the Composer, Genre, and MediaType, and GenreId on the same table 

SELECT Track.Composer, 
       Album.Title,
       MediaType.Name,
       Genre.Name
FROM Track JOIN Album, Genre, MediaType
ON Track.AlbumId = Album.AlbumId
ON Track.MediaTypeId = MediaType.MediaTypeId
ON Track.GenreId = Genre.GenreId
;



SELECT Track.Composer, 
       MediaType.Name,
       Genre.Name
FROM Track JOIN MediaType
ON Track.MediaTypeId = MediaType.MediaTypeId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name='Pop'
AND MediaType.Name='MPEG audio file'
ORDER BY Track.Composer
;



How many 'Pop' songs have an 'MPEG audio file' type?

SELECT COUNT(MediaType.Name)
FROM Track JOIN MediaType
ON Track.MediaTypeId = MediaType.MediaTypeId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name='Pop'
AND MediaType.Name='MPEG audio file'
;

SELECT COUNT(Genre.Name)
FROM Track JOIN MediaType
ON Track.MediaTypeId = MediaType.MediaTypeId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name='Pop'
AND MediaType.Name='MPEG audio file'
;