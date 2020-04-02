# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
  songplay_id bigint PRIMARY KEY,
  start_time timestamp,
  user_id int,
  level varchar,
  song_id varchar REFERENCES songs,
  artist_id varchar REFERENCES artists,
  session_id int,
  location varchar,
  user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
  user_id int PRIMARY KEY,
  first_name varchar,
  last_name varchar,
  gender char(1),
  level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
  song_id varchar PRIMARY KEY,
  title varchar NOT NULL,
  artist_id varchar,
  year int,
  duration numeric NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
  artist_id varchar PRIMARY KEY,
  name varchar NOT NULL,
  location varchar,
  latitude numeric,
  longitude numeric
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  start_time timestamp PRIMARY KEY,
  hour int,
  day int,
  week int,
  month int,
  year int,
  weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, year, duration)
VALUES (%s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id
FROM songs s
JOIN artists a ON (s.artist_id = a.artist_id)
WHERE s.title = %s
AND a.name = %s
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, songplay_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]