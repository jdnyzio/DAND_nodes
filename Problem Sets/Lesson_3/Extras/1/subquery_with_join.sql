SELECT Album.Title, Artist.Name 
FROM Album JOIN Artist 
ON Artist.ArtistId = Album.ArtistId;


#Query
SELECT Track.Composer, Track.Name, Genre.Name, Track.Milliseconds
FROM Track JOIN Genre, 
    (SELECT avg(Milliseconds) as av 
     FROM Track) as subq 
WHERE Milliseconds > av;
ON Track.GenreId=Genre.GenreId;





