
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

#Build this table

DROP TABLE IF EXISTS [Customer];

CREATE TABLE [Customer]
(
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [Country] NVARCHAR(40),
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



