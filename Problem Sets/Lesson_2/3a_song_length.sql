#This time you're on your own!  See if you can translate the following question into a 
query that answers the following question.

#Remember to break down the question if you find that it helps you piece the query together better.  
#You can do it!

#Question: Which tracks in the dataset are between 2500000 and 2600000 milliseconds long?
#Return both the name of the track and the milliseconds of each track in descending order.

SELECT Name, Milliseconds 
FROM Track 
WHERE Milliseconds > 2500000 
AND Milliseconds < 2600000
ORDER BY Milliseconds 
DESC;


SELECT COUNT(Name), Milliseconds 
FROM Track 
WHERE Milliseconds > 2500000 
AND Milliseconds < 2600000
ORDER BY Milliseconds 
DESC;

How many songs have a unit price higher than $1
SELECT avg(Milliseconds), UnitPrice
FROM Track
WHERE UnitPrice = .99
OR UnitPrice < 1.99;
