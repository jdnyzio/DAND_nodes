##  You'll need to decide which musicians you want to invite to play at the event.  
##  Since you've found rock music to be the most popular genre both overall and in Prague, 
##  you'll want to throw a rock concert.  Can you find the 10 rock bands with the most tracks
##  in the rock genre?

'''

Write a query that returns the Artist name, and total track count of the top 10 rock bands. 

'''

QUERY ='''
SELECT Artist.Name as Artist, COUNT(Genre.Name) as count
FROM Genre 
JOIN Track ON Genre.GenreId = Track.GenreId
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Genre.Name = 'Rock'
GROUP BY Artist
ORDER BY count
DESC
LIMIT 10;
'''

