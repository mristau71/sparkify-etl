# sparkify-etl
The purpose of this ETL pipeline is to extract data from the raw song and log data files collected by the fictional Sparkify startup and load them into a database schema designed to optimize queries on song-play analysis.

### Song data
This shows an example of one entry from a song data file:
```javascript
{
  "num_songs": 1,
  "artist_id": "ARMJAGH1187FB546F3",
  "artist_latitude": 35.14968,
  "artist_longitude": -90.04892,
  "artist_location": "Memphis, TN",
  "artist_name": "The Box Tops",
  "song_id": "SOCIWDW12A8C13D406",
  "title": "Soul Deep",
  "duration": 148.03546,
  "year": 1969
}
```

### Log data
This shows an example of one entry from a log data file:
```javascript
{
  "index": 2,
  "artist": "Des'ree",
  "auth": "Logged In",
  "firstName": "Kaylee",
  "gender": "F",
  "itemInSession": 1,
  "lastName": "Summers",
  "length": 246.30812,
  "level": "free",
  "location": "Phoenix-Mesa-Scottsdale, AZ",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1540344794796,
  "sessionId": 139,
  "song": "You Gotta Be",
  "status": 200,
  "ts": 1541106106796,
  "userAgent": "\"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36\"",
  "userId": 8
}
```

## Local setup
You can work with this project locally by having an environment with the following (or equivalent):

- macOS 10.14.6.
- Homebrew 2.2.11. [Installation](https://brew.sh/).
- Python 3.7.7 and pip 20.0.2. Install both with Homebrew: `brew install python`.
- psycopg2 2-2.8.4. Install with pip3: `pip3 install psycopg2`.
- PostgreSQL 9.5.4. [Installation](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb).

**The above could not be tested, as there were problems installing the psycopg2 library with pip3. I will be using Udacity's project workspace to develop the project and use this git project solely to track the development.**

### How to Run

For the initial database creation, run `python create_tables.py`.

To run the ETL, run `python etl.py`.

### Test and Helper Files

The `test.ipynb` file is used to verify the records that have been loaded into the database.

The `etl.ipynb` file is used to test implementation of specific functions that are used in the `etl.py`.

The `sql_queries.py` file is a helper file that contains the queries to create/drop tables, insert records, and select a result set from the database.