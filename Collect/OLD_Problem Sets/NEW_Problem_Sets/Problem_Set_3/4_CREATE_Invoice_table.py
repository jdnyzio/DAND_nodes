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