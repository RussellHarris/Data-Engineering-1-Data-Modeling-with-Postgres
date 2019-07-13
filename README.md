# PURPOSE
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# FILES
* **test.ipynb** - displays the first few rows of each table to let you check your database.
* **create_tables.py** - drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
* **etl.ipynb** - reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
* **etl.py** - reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
* **sql_queries.py** - contains all your sql queries, and is imported into the last three files above.
* **read_data.ipynb** - displays the first few lines of song and log data for visual inspection.

# DESIGN Schema (songplays is the "center" of the star schema)
* **songplays** - (songplay_id serial PRIMARY KEY, start_time timestamp references time(start_time), user_id int references users(user_id), level text, song_id text references songs(song_id), artist_id text references artists(artist_id), session_id int, location text, user_agent text)  
  * songplay_id is an incremented sequence to track each entry inserted from the log
  * songplays requires foreign keys from users, songs, artists, and time
   
* **users** - (user_id int PRIMARY KEY, first_name text, last_name text, gender char(1), level text)  
  * unlike other text fields with variable length, gender only contained one character and was set as char(1)
  * UPSERT: if PRIMARY KEY already exists, update all records with new data
   
* **songs** - (song_id text PRIMARY KEY, title text, artist_id text, year int, duration double precision)  
  * duration set as 'double precision' in order to match log data to populate songplays table
  * UPSERT: if PRIMARY KEY already exists, update all records with new data

* **artists** - (artist_id text PRIMARY KEY, name text, location text, lattitude double precision, longitude double precision)
  * lattitude and longitude stored as double precision
  * UPSERT: if PRIMARY KEY already exists, update all records with new data.

* **time** - (start_time timestamp PRIMARY KEY, hour int, day int, week int, month int, year int, weekday int)
  * start_time includes date+time
  * UPSERT: if PRIMARY KEY already exists, update all records with new data.

# INSTRUCTIONS
* Run the following in order:
1. python create_tables.py
2. python etl.py
3. Check results using tests.ipynb

# EXAMPLE QUERIES
1. Check counts of tables:  
   SELECT 'songs' as table_name, count(*) from songs \
   UNION ALL \
   SELECT 'artists' as table_name, count(*) from artists \
   UNION ALL \
   SELECT 'users' as table_name, count(*) from users \
   UNION ALL \
   SELECT 'songplays' as table_name, count(*) from songplays \
   UNION ALL \
   SELECT 'time' as table_name, count(*) from time;
   
2. Check songplays table for song_id and artist_id matches:  
   SELECT * \
   FROM songplays \
   WHERE song_id <> 'None' \
         AND artist_id <> 'None'
