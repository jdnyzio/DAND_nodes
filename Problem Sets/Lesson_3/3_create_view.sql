#Invoices over average view

CREATE VIEW over_avg_invoice AS
SELECT Customer.FirstName, 
       Customer.LastName, 
       Invoice.BillingCity, 
       Invoice.BillingState,  
       Invoice.BillingCountry, 
       Invoice.Total 
FROM Invoice JOIN Customer, 
    (SELECT avg(Total) as av 
     FROM Invoice) as subq 
WHERE Total > av;
ON Customer.CustomerId=Invoice.CustomerId;







