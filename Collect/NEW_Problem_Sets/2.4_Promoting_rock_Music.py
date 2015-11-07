##  Rock Music Lives on!  After the success of your Previous email campaign, you're interested in 
##  targeting your long standing Rock Music audience!  We'll need to collect a list of emails containing
##  your Rock listeners.  Return their full name, email, and Genre "rock" to be certain you've ##  got the right people.
##  Can you find a way to remove duplicate emails so no one receives multiple emails?


----------------------------------BEFORE QUERY--------------------------------------------
'''

##############     ###############     #################     ############      ###########
#  Customer  #     #  Invoice    #     #  InvoiceLine  #     #  Track   #      #  Genre  # 
##############     ###############     #################     ############      ###########
| CustomerId | --> | CustomerId  |     |  TrackId      | --> | TrackId  |      |  Name   |
+============+     +=============+     +===============+     +==========+      +=========+
| FirstName  |     |  InvoiceId  | --> |  InvoiceId    |     | GenreId  | -->  | GenreId |
+============+     +=============+     +===============+     +==========+      +=========+
|  LastName  |                                                  
+============+
|   Email    |                                                              
+============+

'''
----------------------------------QUERY--------------------------------------------------

QUERY ='''
SELECT Customer.FirstName, Customer.LastName, Customer.Email as Email, Genre.Name
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name="Rock"
GROUP BY Email;

'''
----------------------------------AFTER QUERY----------------------------------------------
'''

###############################################
#                 CustomerGenre               #   <-----RESULT!
###############################################
|  FirstName  |  LastName  |  Email  |  Name  |
+=============+============+=========+========+

'''