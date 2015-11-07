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

'''
Table: Invoice
+------------------------+---------------+-----------------+--------------+
|      Columns           |   Data Type   |    Primary Key  |  Foreign Key |
+========================+===============+=================+==============+ 
|      InvoiceId              INTEGER            YES              NO      |
|      CustomerId             INTEGER            NO               YES     |
|      InvoiceDate            TEXT               NO               NO      |
|      BillingAddress         TEXT               NO               NO      |
|      BillingCity            TEXT               NO               NO      |
|      BillingState           TEXT               NO               NO      |
|      BillingCountry         TEXT               NO               NO      |
|      BillingPostalCode      INTEGER            NO               NO      |
|      Total                  REAL               NO               NO      |
+========================+===============+=================+==============+ 
'''

IMPORT CSV DATA USING .import


QUERY ='''
CREATE TABLE Invoice(
    InvoiceId INTEGER PRIMARY KEY,
    CustomerId INTEGER,
    InvoiceDate TEXT,
    BillingAddress TEXT,
    BillingCity TEXT
    BillingState TEXT
    BillingCountry TEXT
    BillingPostalCode INTEGER
    Total REAL,
    FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId) 
);

''' 