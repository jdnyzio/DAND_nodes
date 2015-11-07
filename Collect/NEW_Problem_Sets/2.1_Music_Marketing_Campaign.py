##  In this problem set you'll be working with new tables in the Chinook database.
##  Previously, you performed queries using parts of the Album, Artist, and Track tables.
##  In this section, you'll also be using the Customer, Invoice, InvoiceLine, and 
##  Genre tables to help drive a marketing campaign that connects your music 
##  to your customers!

''' 
###############  ###################   ##################  ###############   ###########
#  Customer  #   #   Invoice       #   #  InvoiceLine   #  #    Track    #   #  Genre  #
###############  ###################   ##################  ###############   ###########
|  CustomerId |  | InvoiceId        |  | InvoiceLineId  |  |  TrackId    |   | GenreId |
+=============+  +==================+  +================+  +=============+   +=========+
|  FirstName  |  | CustomerId       |  | InvoiceId      |  |  Name       |   |  Name   |
+=============+  +==================+  +================+  +=============+   +=========+
|  LastName   |  | BillingAddress   |  |  TrackId       |  |  AlbumId    |
+=============+  +==================+  +================+  +=============+    
|  Company    |  | BillingCity      |  |  UnitPrice     |  |  MediaTypeId|
+=============+  +==================+  +================+  +=============+    
|  Address    |  | BillingState     |  |  Quantity      |  |  GenreId    |
+=============+  +==================+  +================+  +=============+    
|  City       |  | BillingCountry   |                      |  Composer   |
+=============+  +==================+                      +=============+    
|  State      |  | BillingPostalCode|                      | Milliseconds|
+=============+  +==================+                      +=============+    
|  Country    |  |  Total           |                      |  Bytes      |
+=============+  +==================+                      +=============+    
|  PostalCode |                                            |  UnitPrice  |
+=============+                                            +=============+ 
|  Phone      |
+=============+
|  Fax        |
+=============+
|  Email      |
+=============+
| SupportRepId|
+=============+

'''

