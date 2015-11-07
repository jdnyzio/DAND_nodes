#Now we'll practice using JOINS in the Chinook database.

#QUESTION: List the Albums written by the artist Iron Maiden.  

#Below is an example of a JOIN you've seen in class.
#You can use this example to help compose your new JOIN.

#SELECT animals.name, animals.species, diet.food
#FROM animals JOIN diet
#ON animals.species = diet.species;


#Your Query
SELECT Artist.Name, Album.Title
FROM Album 
JOIN Artist 
ON Artist.ArtistId = Album.ArtistId 
WHERE Name ='Santana' 
OR Name ='Amy Winehouse'
OR Name= 'Eric Clapton'
OR Name='Frank Sinatra';

'''
TABLE 1: Artist
+------------------+---------------+
|      ArtistId    |      Name     |
+==================+===============+
|       59	       |  Santana      |
|       252        |  Amy Winehouse|
|       81         |  Eric Clapton |
+==================+===============+

TABLE 2: Album 
+------------------+-----------------------+-----------+
|      AlbumId     |          Title        |  ArtistId |
+==================+=======================+===========+
|        197       |  As Years Go By       |     59    |
|        198       |  Santana Live         |     59    |
|        321       |  Back to Black        |     252   |
|        322       |  Frank                |     252   |
|        72        |  The Cream Of Clapton |     81    |
|        73        |  Unplugged            |     81    |
+==================+=======================+===========+
'''
