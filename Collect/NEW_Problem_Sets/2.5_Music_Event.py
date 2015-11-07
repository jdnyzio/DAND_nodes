
##  You'd like to throw a promotional music event in the city with the best customers!
##  What city have you made the most money from?


----------------------------------BEFORE QUERY--------------------------------------------

'''

Write a query that returns the BillingCity and Total number of invoices.  
Your query should return 1 row and that row should be the city with the most invoices.

'''

----------------------------------QUERY---------------------------------------------------

QUERY ='''
SELECT BillingCity, sum(Total) as Total
FROM Invoice
GROUP BY BillingCity
ORDER BY Total
DESC
LIMIT 1;
'''
----------------------------------AFTER QUERY----------------------------------------------

'''
##################################   
#          Invoice               #   <-----  RESULT!
##################################   
|  BillingCity  |  sum(Total)    |
+===============+================+
|   Top City      Total Invoices |
+---------------+----------------+

'''

