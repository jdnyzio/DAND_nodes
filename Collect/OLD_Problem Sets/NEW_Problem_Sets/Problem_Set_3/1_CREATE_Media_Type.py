'''
Table: MediaType
+------------------------+---------------+-----------------+-------------------------+
|      Columns           |   Data Type   |    Primary Key  |  Foreign Key/References |
+========================+===============+=================+=========================+ 
|      MediaTypeId            INTEGER            YES              NO                 |
|      Name                   TEXT               NO               NO                 |
+========================+===============+=================+=========================+ 
'''
'''
Here is an example of how tables are created using SQLite.


CREATE TABLE table_name(
  column_1   INTEGER PRIMARY KEY, 
  column_2   TEXT
);

'''

#Try using the information above to build the Invoice table!

QUERY ='''
CREATE TABLE MediaType(
    MediaTypeId INTEGER PRIMARY KEY,
    Name TEXT
);
''' 

INSERT INTO MediaType(MediaTypeId, Name) VALUES (1, "MPEG audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (2, "Protected AAC audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (3, "Protected MPEG-4 video file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (4, "Purchased AAC audio file");
INSERT INTO MediaType(MediaTypeId, Name) VALUES (5, "AAC audio file");