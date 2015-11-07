#In this problem set, you'll practice constructing queries from a given question.  

#Sometimes it's useful to break down more complex questions into smaller components.
#You can then use these smaller pieces to help piece together your query.

#QUESTION: What 10 composers have written the most songs in our dataset?
#Your query should return the composers name followed by the total 
#number of songs they've written in the dataset.

#Step 1: What are you trying to find out?
#Answer: The amount of songs written by the most prolific composers in the dataset.

#Step 2: What table do you need to look at?
#ANSWER: Track

#Step 3: What columns will you need for the query?
#ANSWER: Composer, a count of the number of songs

#Step 4: Do you need to do anything with this column?
#ANSWER: COUNT(*)

#Step 5: How should they be ordered?
#ANSWER: descending, DESC

#Step 6: How many records do you want to see?
ANSWER: The top 10.  LIMIT 10

#Now you can put it all together!
#Use the questions above to fill in the query structure below to build your query!

SELECT Composer, COUNT(*)
FROM Track 
GROUP BY Composer
ORDER BY COUNT(*)
DESC
LIMIT 10;