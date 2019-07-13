# DROP TABLES
#logdata_table_drop = "DROP TABLE IF EXISTS logdata"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
#logdata_table_create = ("""
#CREATE TABLE IF NOT EXISTS logdata (artist text, auth text, firstName text, gender char(1), itemInSession int, lastName text, #length double precision, level text, location text, method text, page text, registration bigint, sessionId int, song text, status #int, ts bigint, userAgent text, userId int);
#""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp REFERENCES time(start_time), user_id int REFERENCES users(user_id), level text, song_id text REFERENCES songs(song_id), artist_id text REFERENCES artists(artist_id), session_id int NOT NULL, location text NOT NULL, user_agent text NOT NULL);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL, gender char(1) NOT NULL, level text NOT NULL)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id text PRIMARY KEY, title text NOT NULL, artist_id text NOT NULL, year int, duration double precision NOT NULL)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id text PRIMARY KEY, name text NOT NULL, location text, lattitude double precision, longitude double precision)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL)
""")

# INSERT RECORDS
#logdata_table_insert = ("""
#INSERT INTO logdata (artist, auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, #registration, sessionId, song, status, ts, userAgent, userId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, #%s, %s, %s)
#""")

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO UPDATE
      SET first_name = EXCLUDED.first_name,
          last_name = EXCLUDED.last_name,
          gender = EXCLUDED.gender,
          level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) 
DO UPDATE
      SET title = EXCLUDED.title,
          artist_id = EXCLUDED.artist_id,
          year = EXCLUDED.year,
          duration = EXCLUDED.duration;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO UPDATE
      SET name = EXCLUDED.name,
          location = EXCLUDED.location,
          lattitude = EXCLUDED.lattitude,
          longitude = EXCLUDED.longitude;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO NOTHING;
""")

# FIND SONGS
song_select = ("""
SELECT s.song_id, 
       s.artist_id
  FROM songs s
       JOIN artists a
         ON s.artist_id = a.artist_id
 WHERE s.title = %s
       AND a.name = %s
       AND s.duration = %s
""")

# QUERY LISTS
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]

#create_table_queries = [logdata_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
#drop_table_queries = [logdata_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]