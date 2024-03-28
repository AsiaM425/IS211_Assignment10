CREATE TABLE Artist (
    artist_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Album (
    album_id INTEGER PRIMARY KEY,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE Song (
    song_id INTEGER PRIMARY KEY,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    duration_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album(album_id)
);
