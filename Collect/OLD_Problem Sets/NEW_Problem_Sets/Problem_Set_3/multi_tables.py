##  This exercise isn't graded but you'll need to use
##  your new table making skills to get the following tables into your 
##  local database.  
##  You'll use these tables to help you get through the rest of the problem set.

##  Each data file is in a different format but SQLite can handle all of them!
##  Once you've got your tables, use the information from the previous reading 
##  to help import all your new data.

##  You can check out the data in the track.sql, customer.csv, and invoice.tsv file tabs, 
##  or you can get them from the downloadables section below.
##  Good luck! If you run into trouble during any of these independent exercises
##  you can reach out to the forums for some advice :)

'''

Use the previous example to help you put together the customer table.  
Include each of the 
'''


#####################################################################
#                         Table: Customer                           #
#####################################################################
+------------------+---------------+-----------------+--------------+
|      Columns     |   Data Type   |    Primary Key  |  Foreign Key |
+==================+===============+=================+==============+ 
|      CustomerId         INTEGER          YES              NO      |
|      FirstName          TEXT             NO               NO      |
|      LastName           TEXT             NO               NO      |
|      Company            TEXT             NO               NO      |
|      Address            TEXT             NO               NO      |
|      City               TEXT             NO               NO      |
|      State              TEXT             NO               NO      |
|      Country            TEXT             NO               NO      |
|      PostalCode         TEXT             NO               NO      |
|      Phone              TEXT             NO               NO      |
|      Fax                TEXT             NO               NO      |
|      Email              TEXT             NO               NO      |
|      SupportRepId       TEXT             NO               YES     |
+==================+===============+=================+==============+ 
'''


'''
The data for this table can be found in invoice.tsv.

###########################################################################
#                         Table: Invoice                                  #
###########################################################################
+------------------------+---------------+-----------------+--------------+
|      Columns           |   Data Type   |    Primary Key  |  Foreign Key |
+========================+===============+=================+==============+ 
|      InvoiceId              INTEGER            YES              NO      |
|      CustomerId             INTEGER            NO               YES     |
|      InvoiceDate            DATETIME           NO               NO      |
|      BillingAddress         TEXT               NO               NO      |
|      BillingCity            TEXT               NO               NO      |
|      BillingState           TEXT               NO               NO      |
|      BillingCountry         TEXT               NO               NO      |
|      BillingPostalCode      INTEGER            NO               NO      |
|      Total                  REAL               NO               NO      |
+========================+===============+=================+==============+ 
'''
