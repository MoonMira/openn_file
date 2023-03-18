CREATE TABLE IF NOT EXISTS Genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artist (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre_artist (
	genre_id INTEGER REFERENCES Genre(id),
	artist_id INTEGER REFERENCES Artist(id),
	CONSTRAINT pk_Genre_artist PRIMARY KEY (genre_id, artist_id)
);


CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) unique NOT NULL,
	year_of_release INTEGER
);


CREATE TABLE IF NOT EXISTS Artist_album (
	album_id INTEGER REFERENCES Album(id),
	artist_id INTEGER REFERENCES Artist(id),
	CONSTRAINT pk_Artist_album PRIMARY KEY (album_id, artist_id)
);


CREATE TABLE IF NOT EXISTS Track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	duration INTEGER,
	album_id INTEGER REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) unique NOT NULL,
	year_of_release INTEGER
);

CREATE TABLE IF NOT EXISTS Collection_track (
	track_id INTEGER REFERENCES Track(id),
	collection_id INTEGER REFERENCES Collection(id),
	CONSTRAINT pk_Collection_track PRIMARY KEY (track_id, collection_id)
);