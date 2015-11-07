'''
Table: Track
+------------------+---------------+-----------------+--------------+
|      Columns     |   Data Type   |    Primary Key  |  Foreign Key |
+==================+===============+=================+==============+ 
|      TrackId         INTEGER            YES              NO       |
|      Name            TEXT               NO               NO       |
|      AlbumId         INTEGER            NO               YES      |
|      MediaTypeId     INTEGER            NO               YES      |
|      GenreId         INTEGER            NO               YES      |
|      Composer        TEXT               NO               NO       |
|      Milliseconds    INTEGER            NO               NO       |
|      Bytes           INTEGER            NO               NO       |
|      UnitPrice       REAL               NO               NO       |
+==================+===============+=================+==============+ 
'''
'''
Here is an example of how tables are created using SQLite.


CREATE TABLE table_name(
  column_1     INTEGER PRIMARY KEY, 
  column_2   TEXT, 
  column_3 INTEGER,
  FOREIGN KEY(column_3) REFERENCES other_table(column_3_equivalent)
);
'''

QUERY ='''
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

''' 