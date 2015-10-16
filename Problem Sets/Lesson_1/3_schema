#The columns in a database make up its schema.  Knowing the schema helps 
#you query the table by knowing what actually exists in the table to be queried.  

#Can you find the schema of the track table and fill in the missing values?

CREATE TABLE [Track]
(
    [-----] INTEGER  NOT NULL,
    [Name] NVARCHAR(200)  --- ----,
    [AlbumId] INTEGER,
    [MediaTypeId] -----  NOT NULL,
    [GenreId] INTEGER,
    [Composer] NVARCHAR(220),
    [----------] INTEGER  NOT NULL,
    [Bytes] INTEGER,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    CONSTRAINT [PK_Track] ------ ---  ([TrackId]),
    FOREIGN KEY ([AlbumId]) REFERENCES [Album] ([AlbumId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([GenreId]) REFERENCES [Genre] ([GenreId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    ------ --- ([MediaTypeId]) REFERENCES [MediaType] ([MediaTypeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
