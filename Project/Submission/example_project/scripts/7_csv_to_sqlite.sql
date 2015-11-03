CREATE TABLE [PlaylistTrack]
(
    [PlaylistId] INTEGER,
    [TrackId] INTEGER,
    CONSTRAINT [PK_PlaylistTrack] PRIMARY KEY  ([PlaylistId], [TrackId]),
    FOREIGN KEY ([PlaylistId]) REFERENCES [Playlist] ([PlaylistId]) 
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId]) 
);

######################################################################

CREATE TABLE [nodes_tags]
(
    [id] INTEGER, 
    [type] TEXT,
    [key] TEXT,
    [value] TEXT
);


######################################################################


CREATE TABLE [nodes]
(
    [id] INTEGER, 
    [lat] REAL,
    [long] REAL,
    [version] TEXT,
    [changeset] INTEGER,
    [timestamp] STRING,
    [user] STRING,
    [uid] INTEGER
);

######################################################################

CREATE TABLE [ways_nodes]

(
    [id] INTEGER, 
    [node_id] INTEGER,
    [position] INTEGER
);


######################################################################

CREATE TABLE [ways_tags]
(
    [id] INTEGER, 
    [type] TEXT,
    [key] TEXT,
    [value] TEXT
);

######################################################################

CREATE TABLE [ways]
(
    [id] INTEGER, 
    [version] TEXT,
    [changeset] INTEGER,
    [timestamp] TEXT,
    [user] TEXT,
    [uid] INTEGER
);

