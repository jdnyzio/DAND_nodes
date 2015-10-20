#Now try a JOIN on your own!

#QUESTION: Build a query that gets the Playlist Name and TrackId
#into the same table and lists them in descending order.

SELECT PlaylistTrack.TrackId, Playlist.Name
FROM PlaylistTrack JOIN Playlist 
ON PlaylistTrack.PlaylistId = Playlist.PlaylistId 
ORDER BY TrackId 
DESC;
