
#Class example
CREATE VIEW course_size as 
SELECT course_id, COUNT(*) as num
FROM enrollment
GROUP by course_id;


#Query
CREATE VIEW over_avg_ms AS
SELECT Track.Composer, Track.Name, Genre.Name, Track.Milliseconds
FROM Track JOIN Genre, 
    (SELECT avg(Milliseconds) as av 
     FROM Track) as subq 
WHERE Milliseconds > av;
ON Track.GenreId=Genre.GenreId;


#Query2
CREATE VIEW over_avg_ms AS
SELECT Track.Composer, Genre.Name, Track.Milliseconds
FROM Track JOIN Genre, 
    (SELECT avg(Milliseconds) AS av 
     FROM Track) AS subq 
WHERE Milliseconds > av;
ON Track.GenreId=Genre.GenreId;