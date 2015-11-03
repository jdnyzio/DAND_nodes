'''
Welcome to your first Problem Set!  Let's start off by jumping into a table of data.

You'll notice the SQL language pretty closely mirrors how you may think 
of questions in your own language.
Maybe you can figure out what the query will return before running it?

You can add, edit, or delete anything you want...this playground is yours.
See if you can come up with something TOTALLY NEW!!  Nothing here is graded so go explore :)
'''
################################################################################
                        
#Chinook Database Schema

'''
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

################################################################################

'''QUESTION: Which songs in this dataset were written by Van Halen?
'''

'''
##################
#      Track     #   <----- FROM
##################
|     Composer   |   <----- SELECT
+================+
|    Van Halen   |   <----- WHERE
+----------------+                                         
'''

#QUERY = 
'''
SELECT Name 
FROM Track 
WHERE Composer='Van Halen';
'''

################################################################################

'''

QUESTION: Your Question Here!

####################################################
#                   Track                          #  <----- FROM
####################################################
|     Composer               |  sum(Milliseconds)  |  <----- SELECT
+============================+=====================+
|    Wolfgang Amadeus Mozart |                        <----- WHERE
+----------------------------+                                         

'''

#QUERY = 
'''
SELECT Composer, sum(Milliseconds) 
FROM Track 
WHERE Composer='Wolfgang Amadeus Mozart';
'''

################################################################################

'''

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

#QUERY=
'''
SELECT Album.Title, Track.Composer, Track.Name
FROM Album JOIN Track
ON Album.AlbumId= Track.AlbumId;
'''

################################################################################

'''

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

#QUERY=
'''
SELECT Artist.Name, Album.Title
FROM Artist JOIN Album
ON Artist.ArtistId = Album.ArtistId 
WHERE Name ='Iron Maiden' 
OR Name ='Amy Winehouse';
'''

################################################################################

'''

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

################################################################################

'''
Try coming up with some questions you would like to ask!
'''


