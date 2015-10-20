SELECT name, weight 
FROM players, 
    (SELECT avg(weight) as av
     FROM players) as subq
WHERE weight < av;


SELECT Name, Composer,  Milliseconds, 
FROM Track, 
    (SELECT avg(Milliseconds) as av 
     FROM Track) as subq 
WHERE Milliseconds > av;


