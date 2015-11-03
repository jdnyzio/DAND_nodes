##  Thanking your best Customers! You'd like to send a promotional email out to all 
##  your best customers.  You've decided that anyone with an invoice of at least 10
##  dollars should get an email thanking them and promoting more business.  

##  You'll need a query that returns the full name, email, and invoice total of 
##  these customers.  Order these customers by their invoice total with the highest 
##  amount on top so your biggest customers are sure to be taken care of first!

---------------------BEFORE QUERY-------------------------
'''

###############         ####################   
#  Customer   #         #     Invoice      #   <-----  FROM/JOIN
###############         ####################   
|  CustomerId | = ON  = | CustomerId       |   
+=============+         +==================+  
|  FirstName  |         | Total            |  <-----  WHERE Total > 10.00
+=============+         +==================+  
|  LastName   |     
+=============+                 
|  Email      |               
+=============+

'''
---------------------QUERY-------------------------

QUERY ='''
SELECT Customer.FirstName, Customer.LastName, Customer.Email, Invoice.Total 
FROM Customer
JOIN  Invoice ON Customer.CustomerId = Invoice.CustomerId
WHERE Invoice.Total > 10.00
ORDER BY Invoice.Total
DESC;
'''
---------------------AFTER QUERY-------------------------
'''
###################################################   
#             CustomerInvoice                     #   <-----  RESULT!
###################################################   
|  FirstName  |  LastName  |  Email  |    Total   |
+=============+============+=========+============+
                                       Total > 10
'''









    