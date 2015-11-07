#Bytes above average
#Conserving Space Create a view of 



CREATE VIEW belowAverageBytes AS
SELECT Track.TrackId, Track.Name, Track.Composer, Milliseconds, MediaType.Name 
FROM Track JOIN MediaType 
ON Track.MediaTypeId = MediaType.MediaTypeId, 
    (SELECT avg(Bytes) as av FROM Track) as subquery 
WHERE Bytes < av;

