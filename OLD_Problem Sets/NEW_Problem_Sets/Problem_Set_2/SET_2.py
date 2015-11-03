################################################################################################################################################

#You'd like to run a promotion targeting the 5 countries with the highest number of invoices.  
#First you need to find out who they are.  
#Write a query that returns the 3 countries with the highest number of invoices.

#2.1 - 0

#Here is an example of a similar query from class you should find very helpful!

'''
SELECT COUNT(*) AS num, species
FROM animals
GROUP BY species
ORDER BY num 
DESC;
'''

QUERY ='''
SELECT BillingCountry, COUNT(*) AS totalInvoices
FROM Invoice
GROUP BY BillingCountry
ORDER BY totalInvoices
DESC
LIMIT 5;
'''

################################################################################################################################################

#Thanking your best Customers! You'd like to send a promotional email out to all your best customers.  You've decided that anyone with an invoice of at least 10
#dollars should get an email thanking them and promoting more business.  

#You'll need a query that returns the full name, email, and invoice total of 
#these customers.  Order these customers by their invoice total with the highest amount on top 
#so your biggest customers are sure to be taken care of first!

#2.2 - 1

#Here is an example of a similar query from class you should find very helpful!
'''
SELECT ordernames.name, COUNT(*) AS num
FROM (animals 
JOIN taxonomy ON animals.species = taxonomy.name) AS ani_tax
JOIN ordernames ON ani_tax.t_order = ordernames.t_order
GROUP BY ordernames.name
ORDER BY num 
DESC;
'''

QUERY ='''
SELECT Customer.FirstName, Customer.LastName, Customer.Email, Invoice.Total 
FROM Customer
JOIN  Invoice ON Customer.CustomerId = Invoice.CustomerId
WHERE Invoice.Total > 10.00
ORDER BY Invoice.Total
DESC;
'''
    

################################################################################################################################################

# - 4

#Rock Music Lives on!  After the success of your Previous email campaign, you're interested in 
#targeting your long standing Rock Music audience!  We'll need to collect a list of emails containing
#your Rock listeners.  Return their full name, email, and Genre "rock" to be certain you've got the right people.
#Can you find a way to remove duplicate emails so no one receives multiple emails?

#Here is an example of a similar query from class you should find very helpful!
'''
SELECT ordernames.name, COUNT(*) AS num
FROM (animals 
JOIN taxonomy ON animals.species = taxonomy.name) AS ani_tax
JOIN ordernames ON ani_tax.t_order = ordernames.t_order
GROUP BY ordernames.name
ORDER BY num 
DESC
'''

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

################################################################################################################################################

# - 0

#You'd like to throw a promotional music event in the city with the best customers!
#What city have you made the most money from?

QUERY ='''
SELECT BillingCity, sum(Total) as Total
FROM Invoice
GROUP BY BillingCity
ORDER BY Total
DESC
LIMIT 1;
'''

BillingCity  Total     
-----------  ----------
Prague       90.24   

################################################################################################################################################

# - 3

#Now to throw an event, we need to know what kind of music they like in Prague!  Can you figure out what types of music are selling the best?

QUERY ='''
SELECT Invoice.BillingCity, Genre.Name, COUNT(Genre.Name)
FROM Invoice
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE BillingCity = "Prague"
GROUP BY Genre.Name
ORDER BY COUNT(Genre.Name)
DESC
LIMIT 3;
'''

################################################################################################################################################

# - 3

#Great success,  You'd like to jump on the Prague railway and take your show through France and have a final show in Paris!  
#List Cities in France with the lowest invoice totals on top and their favorite genres of music!


QUERY = '''
SELECT Invoice.BillingCity, Genre.Name, COUNT(Genre.Name) 
FROM Invoice
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE BillingCountry = "France"
GROUP BY Genre.Name
ORDER BY BillingCity, COUNT(Genre.Name)
DESC;
'''