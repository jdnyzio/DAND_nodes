
QUERY ='''
CREATE TABLE MediaType(
    MediaTypeId INTEGER PRIMARY KEY,
    Name TEXT
);
''' 
########################################################################################################################################################################################################

INSERT INTO MediaType(MediaTypeId, Name) VALUES (1, "MPEG audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (2, "Protected AAC audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (3, "Protected MPEG-4 video file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (4, "Purchased AAC audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (5, "AAC audio file");

CREATE TABLE Track(
    TrackId INTEGER PRIMARY KEY,
    Name TEXT,
    AlbumId INTEGER,
    MediaTypeId INTEGER,
    GenreId INTEGER,
    Composer TEXT,
    Milliseconds INTEGER,
    Bytes INTEGER,
    UnitPrice REAL,
    FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId) 
    FOREIGN KEY (GenreId) REFERENCES Genre(GenreId) 
    FOREIGN KEY (MediaTypeId) REFERENCES MediaType(MediaTypeId) 
);

COPY PASTE

########################################################################################################################################################################################################

SELECT MediaType.Name as MediaType, sum(Track.Bytes) as Bytes, COUNT(*) AS Files
FROM Track
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
GROUP BY MediaType.Name;

########################################################################################################################################################################################################

#Based on your query, management has decided that to conserve data we'll be removing Protected MPEG-4 video file from the size.  
#They want to conserve data space and focus on audio files instead.
#They've got a strong userbase and hope to get an email out to their current Protected MPEG-4 video file customers about the transition to give a coupon.They

#We'll need to use SQL to figure out the email of customers that have used Protected MPEG-4 video files with our company.


#First lets make a list that includes all Protected MPEG-4 video files.

CREATE VIEW TrackIdMediaType AS
SELECT Track.TrackId, MediaType.Name
FROM Track
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
WHERE MediaType.Name="Protected MPEG-4 video file";


########################################################################################################################################################################################################


SELECT Customer.Email as Email, Invoice.InvoiceId as Invoice, InvoiceLine.TrackId, Track.TrackId, MediaType.Name
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
WHERE MediaType.Name = "Protected MPEG-4 video file"
GROUP BY Email;

SELECT Customer.FirstName, Customer.LastName, Customer.Email as Email, Invoice.InvoiceId as Invoice, InvoiceLine.TrackId, Track.TrackId, Genre.Name
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = "Pop"
GROUP BY Email;

SELECT Customer.FirstName, Customer.LastName, Customer.Email as Email, Genre.Name
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track ON Track.TrackId = InvoiceLine.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name="Pop" 
GROUP BY Email;



########################################################################################################################################################################################################

CREATE TABLE InvoiceLine(
    InvoiceId INTEGER PRIMARY KEY,
    TrackId TEXT,
    UnitPrice INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (InvoiceId) REFERENCES Invoice(InvoiceId) 
    FOREIGN KEY (TrackId) REFERENCES Track(TrackId) 
);