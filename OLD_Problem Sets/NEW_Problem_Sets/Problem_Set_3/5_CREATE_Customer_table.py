'''
Table: Customer
+------------------+---------------+-----------------+--------------+
|      Columns     |   Data Type   |    Primary Key  |  Foreign Key |
+==================+===============+=================+==============+ 
|      CustomerId         INTEGER           YES              NO     |
|      FirstName          TEXT              NO               NO     |
|      LastName           TEXT              NO               NO     |
|      Company            TEXT              NO               NO     |
|      Address            TEXT              NO               NO     |
|      City               TEXT              NO               NO     |
|      State              TEXT              NO               NO     |
|      Country            TEXT              NO               NO     |
|      PostalCode         TEXT              NO               NO     |
|      Phone              TEXT              NO               NO     |
|      Fax                TEXT              NO               NO     |
|      Email              TEXT              NO               NO     |
|      SupportRepId       INTEGER           NO               YES    |
+==================+===============+=================+==============+ 
'''


QUERY ='''
CREATE TABLE Invoice(
    CustomerId INTEGER PRIMARY KEY,
    FirstName TEXT, 
    LastName TEXT,
    Company TEXT,
    Company TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Country TEXT,
    PostalCode TEXT,
    Phone TEXT,
    Fax TEXT,
    Email TEXT,
    SupportRepId
    FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId) 
);

''' 