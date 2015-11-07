#You'll want to know the MediaType, Bytesize, and Total number of tracks that are in each media type.

#This way you can find out what's costing you all that data and can cut them from the 


#What is the total byte size of all each different Track Media type?

CREATE VIEW bytesNumber AS
SELECT MediaType.Name as MediaType, sum(Track.Bytes) as Bytes, COUNT(*) AS Number
FROM Track
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
GROUP BY MediaType.Name;

AAC audio file              |49244732
MPEG audio file             |26184720875
Protected AAC audio file    |1105319551
Protected MPEG-4 video file |89985654585
Purchased AAC audio file    |61315607

Bytes/Number
------------
4476793     
8630428     
4663795     
420493713   
8759372   


CREATE VIEW joinMediaTypeTrack AS
SELECT Track.TrackId, Track.Milliseconds, Track.Bytes, MediaType.Name
FROM Track
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId;

SELECT * FROM joinMediaTypeTrack LIMIT 10;