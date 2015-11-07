'''

Welcome to your first Problem Set!  
Problem Sets are here to get you set up and ready to do even more amazing things using SQL.

Lets jump right in...

Uncomment the next line query and hit Test Run to see the result of your first query!

'''

QUERY = "SELECT Name FROM Track WHERE Composer='Van Halen';"

'''

NICE WORK!

Throughout the problem sets in this course you'll be using the Chinook Database.

This database represents a music store you're going to explore, market, and eventually build all on your own!

SQL is all about answering questions driven by your own curiosity and excitement about the data you've collected.  

Let's see how well our question translates into an SQL statement.

'''

'''QUESTION:Which songs in this dataset were written by AC/DC?'''

#QUERY = "SELECT Name FROM Track WHERE Composer='AC/DC';"

'''Did you run that query to find out?  Try it!'''


##  You'll also be seeing visual guides within programming quizzes as you move forward!  ##  These are meant to show you how your query and database are working together to ##  get you the information you need :)

'''
--VISUAL GUIDE!--

          ##############          ############          ##################
Tables:   #   Artist   #          #  Album   #          #      Track     # 
          ##############          ############          ##################
Column1:  | ArtistId   | <---|    | AlbumId  | <----    |   TrackId      |
          +============+     |    +==========+     |    +================+ 
Column2:  | Name       |     |    |  Title   |     ---> |   AlbumId      |
          +============+     |    +==========+          +================+
Column3:                     ---> | ArtistId |          |   Name         |
                                  +==========+          +================+
Column4:                                                |   Composer     | 
                                                        +================+     
'''

## Let's do some querying!

##  You'll notice the SQL language pretty closely mirrors how you may think 
##  of questions in your own language.
##  Maybe you can figure out what the query will return before running it?

##  You can add, edit, or delete anything you want...this playground is yours.
##  See if you can come up with something TOTALLY NEW!!  Nothing here is graded so go ##  explore :)

'''QUESTION: Which songs in this dataset were written by Van Halen?'''

#QUERY = "SELECT Name FROM Track WHERE Composer='Van Halen';"

'''
##################
#      Track     #   <----- FROM
##################
|     Name       |   <----- SELECT
+================+
|    Composer    |   <----- WHERE
+================+
'''

################################################################################

QUESTION: Your Question Here!

####################################################
#                   Track                          #  <----- FROM
####################################################
|     Composer               |  sum(Milliseconds)  |  <----- SELECT
+============================+=====================+
|    Wolfgang Amadeus Mozart |                        <----- WHERE
+----------------------------+                                         

'''

#QUERY = "SELECT Composer, sum(Milliseconds) FROM Track WHERE Composer='Wolfgang Amadeus Mozart';"

'''

################################################################################

QUESTION: Your Question Here!

####################          #############################
#      Album       #          #           Track           #   <------  FROM/JOIN
####################          #############################
| Title  | AlbumId |  = ON =  | AlbumId | Name | Composer |   <------  SELECT
+========+=========+          +=========+======+==========+                                          

####################################
#          Album/Track             #
####################################
|  Title  |  Name   |   Composer   |                          <------ RESULT!
+=========+=========+==============+

'''                  

#QUERY= "QUERY= "SELECT Track.Bytes, Album.Title FROM Album JOIN Track ON Track.AlbumId=Album.AlbumId;""

'''

################################################################################


QUESTION: Your Question Here!


#####################         ####################
#      Artist       #         #       Album      #                  <------  FROM/JOIN
#####################         ####################
| Name   | ArtistId | = ON =  | ArtistId | Title |     <------  SELECT
+========+==========+         +==========+=======+

########################
#     ArtistAlbum      # 
########################
| Name         | Title |                               <------ RESULT!
+==============+=======+
| Iron Maiden  |
----------------
| Amy Winehouse|
----------------

'''  


#QUERY="SELECT Artist.Name, Album.Title FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId WHERE Name ='Iron Maiden' OR Name ='Amy Winehouse';"

'''

################################################################################


QUESTION:Which songs in this dataset were written by AC/DC?


##################
#     Track      #      <----- FROM
##################
|     Composer   |   <----- SELECT
+================+
|    ?????????   |   <----- WHERE
+----------------+                                         

'''

#QUERY = 'Your Query Here!'



'''
Try coming up with some questions you would like to ask!
'''


SELECT TrackId, Bytes
FROM Track,
(SELECT avg(Bytes) as average FROM Track) AS subquery
WHERE Bytes < average;