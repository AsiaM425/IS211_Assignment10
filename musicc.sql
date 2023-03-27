artist_id INTEGER PRIMARY KEY,
 artist_name TEXT
);
CREATE TABLE album (
 album_id INTEGER PRIMARY KEY,
 album_name TEXT,
 artist_id INTEGER,
 FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);
CREATE TABLE song (
 song_id INTEGER PRIMARY KEY,
 song_name TEXT,
 album_id INTEGER,
 track_number INTEGER,
 duration INTEGER,
 FOREIGN KEY (album_id) REFERENCES album(album_id)
);
