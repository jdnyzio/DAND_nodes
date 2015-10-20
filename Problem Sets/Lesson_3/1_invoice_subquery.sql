#Invoices over average

SELECT BillingCity, BillingState,  BillingCountry, Total 
FROM Invoice, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;