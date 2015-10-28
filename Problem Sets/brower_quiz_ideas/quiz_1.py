#You've been given the following table which is a subset of customers from the Chinook database.
#Using this table, can you answer the following questions using SQL queries?

'''
TABLE: Customer
+-----------+---------------+-------------+
| FirstName |   LastName    |   Country   |
+===========+===============+=============+ 
|  Daan	    |   Peeters     |  Belgium    |
|  Kara     |   Nielson     |  Denmark    |
|  Roberto  |   Almeida     |  Brazil     |
|  Frank    |   Harris      |  USA        |
|  John     |   Gordon      |  USA        |
|  Isabelle |   Mercier     |  France     |
|  Mark     |   Taylor      |  Australia  |
|  Luis     |   Rojas       |  Chile      |
|  Manoj    |   Pareek      |  India      |
|  Puja     |   Srivastava  |  India      |
+===========+===============+=============+
'''


#Questions to ask

#What are the first names of customers in India?
SELECT FirstName FROM Customer WHERE Country='India';

#What is the last name of our customer in France?
SELECT LastName FROM Customer WHERE Country='France';

#How many of our customers are in the USA?
SELECT COUNT(*) FROM Customer WHERE Country='USA';

#What are the first and last names of customers located in either Australia or Chile?
SELECT FirstName, LastName FROM Customer WHERE Country='Australia' or Country='Chile';

#Put rows in the order last name, first name, and country then list them alphabetically by last name.
SELECT LastName, FirstName, Country FROM Customer ORDER BY LastName;

#How many unique countries are represented in this list?
SELECT COUNT(DISTINCT Country) FROM Customer;

#List all columns of customers from USA, Inida, and Belgium alphabetically by country then by last name.
SELECT FirstName, LastName, Country FROM Customer ORDER BY Country, LastName;

#



#Build this table

DROP TABLE IF EXISTS [Customer];

CREATE TABLE [Customer]
(
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [Country] NVARCHAR(40)
);


INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Daan', 'Peeters', 'Belgium');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Kara', 'Nielson', 'Denmark');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Roberto', 'Almeida', 'Brazil');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Frank', 'Harris', 'USA');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('John', 'Gordon', 'USA');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Isabelle', 'Mercier', 'France');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Mark', 'Taylor', 'Australia');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Luis', 'Rojas', 'Chile');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Manoj', 'Pareek', 'India');
INSERT INTO [Customer] ([FirstName], [LastName], [Country]) VALUES ('Puja', 'Srivastava', 'India');



