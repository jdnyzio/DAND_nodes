##  You'd like to run a promotion targeting the 3 countries with the highest number of invoices.  
##  First you need to find out who they are.  
##  Write a query that returns the 3 countries with the highest number of invoices.


---------------------BEFORE QUERY-------------------------
'''

################
#   Invoice    #              <----- FROM
################ 
| BillingCountry|  COUNT(*)   <----- SELECT
+===============+

'''

---------------------QUERY---------------------------------

QUERY ='''
SELECT BillingCountry, COUNT(*) AS totalInvoices
FROM Invoice
GROUP BY BillingCountry
ORDER BY totalInvoices
DESC
LIMIT 3;
'''

---------------------AFTER QUERY---------------------------
'''

################################
#           Invoice            #   <----- RESULT!
################################  
| BillingCountry|   COUNT(*)   |  
+===============+==============+

'''

