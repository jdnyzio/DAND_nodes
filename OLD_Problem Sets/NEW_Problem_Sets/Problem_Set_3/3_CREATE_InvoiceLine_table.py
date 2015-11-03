'''
Table: InvoiceLine
+------------------------+---------------+-----------------+--------------+
|      Columns           |   Data Type   |    Primary Key  |  Foreign Key |
+========================+===============+=================+==============+ 
|      InvoiceLineId          INTEGER            YES              NO      |
|      InvoiceId              INTEGER            NO               YES     |
|      TrackId                INTEGER            NO               YES      |
|      UnitPrice              REAL               NO               NO      |
|      Quantity               INTEGER            NO               NO      |
+========================+===============+=================+==============+ 
'''



QUERY ='''
CREATE TABLE InvoiceLine(
    InvoiceId INTEGER PRIMARY KEY,
    TrackId TEXT,
    UnitPrice INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (InvoiceId) REFERENCES Invoice(InvoiceId) 
    FOREIGN KEY (TrackId) REFERENCES Track(TrackId) 
);

''' 